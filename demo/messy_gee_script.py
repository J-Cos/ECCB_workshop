import ee
import json

ee.Initialize()

# do stuff
x = ee.Geometry.Polygon([[[108.5, 4.5], [119.5, 4.5], [119.5, -4.5], [108.5, -4.5], [108.5, 4.5]]])

img = ee.Image('UMD/hansen/global_forest_change_2023_v1_11')

# get tree cover
d = img.select('treecover2000').clip(x)

# mask
m = d.gte(30)
d = d.updateMask(m)

# compute
temp = img.select('lossyear').clip(x)
temp = temp.updateMask(m)

# reproject for some reason
temp = temp.reproject(crs='EPSG:4326', scale=30)

result2 = {}
for i in range(1, 24):
    # get loss for year
    r = temp.eq(i)
    r = r.multiply(ee.Image.pixelArea()).divide(10000)  # ha
    out = r.reduceRegion(
        reducer=ee.Reducer.sum(),
        geometry=x,
        scale=30,
        maxPixels=1e13,
        bestEffort=True
    )
    result2[2000 + i] = out.getInfo()['lossyear']

# print it
print("=== BORNEO DEFORESTATION ===")
total = 0
for k in sorted(result2.keys()):
    v = result2[k]
    total = total + v
    print(str(k) + ": " + str(round(v, 2)) + " ha")

print("Total loss: " + str(round(total, 2)) + " ha")

# avg
avg = total / 23
print("Average annual loss: " + str(round(avg, 2)) + " ha")

# tree cover stats
tc_stats = d.reduceRegion(reducer=ee.Reducer.mean(), geometry=x, scale=30, maxPixels=1e13, bestEffort=True).getInfo()
print("Mean tree cover (2000): " + str(round(tc_stats['treecover2000'], 2)) + "%")

# count pixels
px = d.reduceRegion(reducer=ee.Reducer.count(), geometry=x, scale=30, maxPixels=1e13, bestEffort=True).getInfo()
print("Forested pixels (>=30%): " + str(px['treecover2000']))

# area
total_forest_area = px['treecover2000'] * 30 * 30 / 10000  # ha
print("Approx forested area: " + str(round(total_forest_area, 2)) + " ha")

# pct lost
pct = (total / total_forest_area) * 100
print("Percentage of forest lost: " + str(round(pct, 2)) + "%")

# worst year
worst_yr = max(result2, key=result2.get)
print("Worst year: " + str(worst_yr) + " (" + str(round(result2[worst_yr], 2)) + " ha)")

# make a chart kind of
print("\n--- Loss by Year ---")
max_val = max(result2.values())
for k in sorted(result2.keys()):
    v = result2[k]
    bar_len = int((v / max_val) * 50) if max_val > 0 else 0
    print(str(k) + " |" + "#" * bar_len + " " + str(round(v, 1)))

# export (commented out so it doesn't actually run)
# task = ee.batch.Export.image.toDrive(
#     image=temp.clip(x).reproject(crs='EPSG:4326', scale=30),
#     description='borneo_loss',
#     folder='gee_exports',
#     region=x,
#     scale=30,
#     maxPixels=1e13
# )
# task.start()

# gain
g = img.select('gain').clip(x)
g = g.updateMask(m)
gain_stats = g.reduceRegion(reducer=ee.Reducer.sum(), geometry=x, scale=30, maxPixels=1e13, bestEffort=True).getInfo()
gain_px = gain_stats['gain']
gain_area = gain_px * 30 * 30 / 10000
print("\nForest gain pixels: " + str(gain_px))
print("Forest gain area: " + str(round(gain_area, 2)) + " ha")

net = gain_area - total
print("Net change: " + str(round(net, 2)) + " ha")
if net < 0:
    print("WARNING: Net deforestation!")
else:
    print("Net reforestation")

print("\n=== DONE ===")
