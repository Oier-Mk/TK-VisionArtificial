from pylabel import importer
path = "/Users/omentxaka/OneDrive - Teknei/Escritorio/image.txt"
dataset = importer.ImportYoloV5(path)
dataset.export.ExportToVoc(dataset)