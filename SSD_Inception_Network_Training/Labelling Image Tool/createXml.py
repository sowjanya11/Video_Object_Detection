import os
import xml.etree.cElementTree as ET

def removeDStore(directory):
    if '.DS_Store' in directory:
        directory.remove('.DS_Store')

    return directory

def getBoundariesAndId(filename):
    classes = ['appy', 'fanta', 'appyfizz', 'sprite']
    path = 'labels_96/'+filename

    with open(path, 'r') as f:
        row = f.read().rstrip().split(' ')

        class_id = classes[int(row[0])]
        xmin = int(float(row[1])*160)
        ymin = int(float(row[2])*96)
        w = int(float(row[3])*160)
        h = int(float(row[4])*96)
        xmax = xmin + w
        ymax = ymin + h

    return (class_id, xmin, ymin, xmax, ymax)


def createXml(folder, img_filename, img_path, img_attributes, name):
    annotation = ET.Element("annotation")
    ET.SubElement(annotation, "folder").text = folder
    ET.SubElement(annotation, "filename").text = img_filename
    ET.SubElement(annotation, "path").text = img_path

    source = ET.SubElement(annotation, "source")
    ET.SubElement(source, "database").text = "Unknown"

    size = ET.SubElement(annotation, "size")
    ET.SubElement(size, "width").text = "160"
    ET.SubElement(size, "height").text = "96"
    ET.SubElement(size, "depth").text = "3"
    # ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
    ET.SubElement(annotation, "segmented").text = "0"

    object1 = ET.SubElement(annotation, "object")
    ET.SubElement(object1, "name").text = img_attributes[0]
    ET.SubElement(object1, "pose").text = "Unspecified"
    ET.SubElement(object1, "truncated").text = "0"
    ET.SubElement(object1, "difficult").text = "0"

    bndbox = ET.SubElement(object1, "bndbox")
    ET.SubElement(bndbox, "xmin").text = str(img_attributes[1])
    ET.SubElement(bndbox, "ymin").text = str(img_attributes[2])
    ET.SubElement(bndbox, "xmax").text = str(img_attributes[3])
    ET.SubElement(bndbox, "ymax").text = str(img_attributes[4])



    tree = ET.ElementTree(annotation)
    tree.write("training-images-96-xml/" + direc + '/'+ name+".xml")


if __name__ == '__main__':
    root = "training-images-96/"

    dirs = os.listdir(root)
    # print(dirs)
    dirs = removeDStore(dirs)

    for direc in dirs:
        files = os.listdir(root + direc)
        files = removeDStore(files)
        folder = direc

        for file in files:
            img_filename = file
            img_path = root+direc+'/'+file
            name =  file.split('.')[0]
            filename = name + '.txt'

            img_attributes = getBoundariesAndId(filename)

            print(name)
            createXml(folder, img_filename, img_path, img_attributes, name)
            # break

        # break

