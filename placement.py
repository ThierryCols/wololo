import parser
import rawData

rawServerList = rawData.getRawServerList()
serverList = parser.parseInd(rawServerList)


#rowList = [(0, []),(1, []),(2, []),(3, []),(4, []),(5, []),(6, []),(7, []),(8, []),(9, []),(10, []),(11, []),(12, []),(13, []),(14, []),(15, []),]

# print serverList