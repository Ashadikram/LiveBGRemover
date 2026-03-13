import tensorflow as tf

saved_model_dir = "universal-sentence-encoder-tensorflow1-lite-v2"

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)

tflite_model = converter.convert()

with open("use_model.tflite","wb") as f :
    f.write(tflite_model)

print("Conversion completed")

