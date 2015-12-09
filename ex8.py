import time
# One format
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
# single and double quotation mark both turn into single one
print formatter % ('one', "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
# the elements are separated by blank spaces because of commas
print formatter % (
	"I had this thing.",
	"That you could type up right.", 
	"But it didn't sing.",
	"So I said goodnight."
)
# Use "ctrl + c" to stop this script
# print a dynamic snowflake
while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,
		# before print the next element, it stops for 0.01ms
		time.sleep(0.01)