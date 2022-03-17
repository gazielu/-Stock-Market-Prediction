mometum Prediction
==================






https://medium.com/analytics-vidhya/how-to-use-google-colab-with-github-via-google-drive-68efb23a42d


from google.colab import drive
drive.mount('/content/drive')

%cd /content/drive/MyDrive/Github/

###git clone https://{git_token}@github.com/{username}/{repository}
!git clone https://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@github.com/gazielu/Stock-Market-Prediction.git

ls
