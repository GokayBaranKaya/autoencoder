# Autoencoder-Based Image Compression

## Overview
This project evaluates the effectiveness of autoencoder-based image compression methods against conventional image compression algorithms. 
Using the Imagenette dataset, which consists of representative images scaled to 160 pixels on the short side mostly in RGB, this study aims to analyze the quality of compressed images using PSNR and SSIM metrics to identify the most efficient image compression technique.

## Project Steps

- **Preprocess Images**: Standardized image size to 160x160 pixels. Split the dataset into training, validation, and testing sets with a 70/15/15 distribution. For preprocessing details, see [preprocess_images script](https://github.com/GokayBaranKaya/thesis/blob/main/preprocess_images.py).
- **Hyperparameter Search**: Used the Optuna library to empirically search for optimal hyperparameters. For more details, check out [test_models notebook](https://github.com/GokayBaranKaya/thesis/blob/main/test_models.ipynb).
- **Model Training and Image Saving**: Re-trained models with optimal hyperparameters at maximum epochs and saved them. Also saved conventional compression images (JPEG, WebP, TIFF) at various qualities. See [save_models & images notebook](https://github.com/GokayBaranKaya/thesis/blob/main/saving_aemodes%26conv_imgs.ipynb).
- **Evaluation of Metrics**: Predicted, evaluated, and saved compressed images using autoencoder models. Also evaluated conventionally compressed images. For evaluation specifics, visit [evaluation notebook](https://github.com/GokayBaranKaya/thesis/blob/main/evaluation.ipynb).

## Requirements
- Python
- Numpy
- TensorFlow
- Keras
- PIL
- Optuna
- Sckit-image (from skimage)

## Findings
### PSNR Results
![psnr](https://github.com/GokayBaranKaya/thesis/assets/101580584/462cb3ac-621e-4ce8-bd87-6c4e3c7ec817)
### SSIM Results
![ssim](https://github.com/GokayBaranKaya/thesis/assets/101580584/8328d6a6-7a9f-480a-b453-4976d6a1a57a)
### Original-Reconstructed Images
![img20](https://github.com/GokayBaranKaya/thesis/assets/101580584/e0f4ddb4-b5b0-4b7f-8cb7-670b3cfa00ec)
![img40](https://github.com/GokayBaranKaya/thesis/assets/101580584/94dfef82-7d46-49cf-94d6-5a54d52ef99a)
![img80](https://github.com/GokayBaranKaya/thesis/assets/101580584/4dd7007f-698d-40e0-b3ae-c0526afdfcd7)

**Note:** One layer represents 80x80, two layers represents 40x40, and three layer represents 20x20 bottleneck size.

## Conclusuion
The project shows that autoencoder based image compression models can achieve results as high as conventional methods do in terms PSNR and SSIM metrics. Specifically the model with one layer and two layers which achived satisfying results as their compared
conventional methods JPEG and WebP at quality 75 and 50 respectively. However, there is color loss that can be observed, especially with two-layer model. When it comes to the last model, three-layer autoencoder didn't achieve better results than it's compared
conventional methods and even if we do not consider conventional methods, 25.2358 dB PSNR and 0.780254 SSIM scores can be considered as slightly bad.
