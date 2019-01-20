##This explains training SSD_INCEPTION_V2 model for Object detection

1. Resized the data using resize.py
2. Split the data into test and train data randomly (90:10)
3. Labelled the data using selectROI OpenCV method and converting it to XML using python and create xml per each image(see in Tensorflow Model/workspace/training_demo/images folder).
4. Then XML files are converted to csv format for train and test. Then to tfrecord for tensorflow processing.
5. ssd_inception_v2_coco.config is used for pretrained weights
6. Download SSD_Inception_V2 from https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md and unzip under pr-trained-model
6. Once training is done, the inference graph is exported using export_inference_graph.py
7. Then Test the image using objec_detection_image.py


##Note: Not uploading Tensorflow/models