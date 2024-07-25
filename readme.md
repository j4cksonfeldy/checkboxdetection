# Installing Dependncies & Env
https://www.youtube.com/watch?v=rRwflsS67ow
# Steps for training model
1. Gather images and use labelImg for annotations
2. Use data_gen.ipynb to convert xmls & imgs into csvs, then csvs into tf.record files
3. Download pre-trained model for TF Model Zoo
4. Update paths in config files, route checkpoint to model chkpt dir
5. cd to object_detection folder, run last cell of train.ipynb, including paths to train saves & pipeline config
