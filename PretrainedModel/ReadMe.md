##This method explains how to use pretrained model for training new set of images
1. Need to create dataset similar to training_data/cooldrinks
2. Resize the images and decreased brightness and applied rotations to the data.
3. Train using training/retrain.py, it creates /tmp/output_graph.pb and /tmp/output_labels.txt
4. The training is not too long.
5. Then we can test the model using label_image.py
6. Since the test images are dark and the objects are too small(thumbnails), I have cropped constant area in the image and then increased brightness(edited_thumbnails).
7. Then applied grabcut to separate background from the object(grabcut_results)
