﻿$pathToSourceRoot = "C:\Users\Alex\Repositories\MusicSymbolClassifier\HomusTrainer\"
$pathToTranscript = "$($pathToSourceRoot)"

# Allowing wider outputs https://stackoverflow.com/questions/7158142/prevent-powergui-from-truncating-the-output
$pshost = get-host
$pswindow = $pshost.ui.rawui
$newsize = $pswindow.buffersize
$newsize.height = 9999
$newsize.width = 1500
$pswindow.buffersize = $newsize
#$newsize = $pswindow.windowsize
#$newsize.height = 50
#$newsize.width = 150
#$pswindow.windowsize = $newsize

cd $pathToSourceRoot
echo "Appending source root $($pathToSourceRoot) to temporary PYTHONPATH"
$env:PYTHONPATH = $pathToSourceRoot

#python C:\Users\Alex\Repositories\MusicSymbolClassifier\HomusTrainer\tests\Symbol_test.py
#cd "tests"
#pytest


################################################
# Trainings not yet started
################################################

##### Evaluating different optimizers on the same data, with/without LR-Reduction

# Not yet started
Start-Transcript -path "$($pathToTranscript)2017-06-xx_vgg_staff88.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg -s 3 -offsets 88 --width 128 --height 224 --minibatch_size 64 --optimizer SGD
Stop-Transcript

# Not yet started
Start-Transcript -path "$($pathToTranscript)2017-06-xx_vgg_staff88.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg -s 3 -offsets 88 --width 128 --height 224 --minibatch_size 64 --optimizer Adadelta
Stop-Transcript

# Not yet started
Start-Transcript -path "$($pathToTranscript)2017-06-xx_vgg_staff88.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg -s 3 -offsets 88 --width 128 --height 224 --minibatch_size 64 --optimizer Adadelta --no_dynamic_learning_rate_reduction
Stop-Transcript

# Not yet started
Start-Transcript -path "$($pathToTranscript)2017-06-xx_vgg_staff88.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg -s 3 -offsets 88 --width 128 --height 224 --minibatch_size 64 --optimizer Adam
Stop-Transcript

# Not yet started
Start-Transcript -path "$($pathToTranscript)2017-06-xx_vgg_staff88.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg -s 3 -offsets 88 --width 128 --height 224 --minibatch_size 64 --optimizer Adam --no_dynamic_learning_rate_reduction
Stop-Transcript


##### Evaluating different line-thicknesses

# Not yet started
Start-Transcript -path "$($pathToTranscript)2017-06-xx_vgg_stroke2_staff74-81-88-95.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg -s 2 -offsets 74,81,88,95 --width 128 --height 224 --minibatch_size 16/64 --optimizer Adadelta
Stop-Transcript

# Not yet started
Start-Transcript -path "$($pathToTranscript)2017-06-xx_vgg4_stroke2_staff74-81-88-95.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg4 -s 2 -offsets 74,81,88,95 --width 128 --height 224 --minibatch_size 16/64 --optimizer Adadelta
Stop-Transcript


##### Large dataset with vgg
Start-Transcript -path "$($pathToTranscript)2017-06-xx_vgg_stroke1-2-3_staff74-81-88-95.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg -s 1,2,3 -offsets 74,81,88,95 --width 128 --height 224 --minibatch_size 16/64 --optimizer Adadelta
Stop-Transcript


##### Smaller image-sizes

# Not yet started
Start-Transcript -path "$($pathToTranscript)2017-06-xx_vgg4_staff74_192x96.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg4 -s 3 -offsets 74 --width 96 --height 192 --minibatch_size 64 --optimizer Adadelta
Stop-Transcript

# Not yet started
Start-Transcript -path "$($pathToTranscript)2017-06-08_vgg_staff60-67-74-81_192x96.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg -s 3 -offsets 60,67,74,81 --width 96 --height 192 --minibatch_size 64 --optimizer Adam
Stop-Transcript

# Not yet started
Start-Transcript -path "$($pathToTranscript)2017-06-08_vgg4_staff60-67-74-81_192x96.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg4 -s 3 -offsets 60,67,74,81 --width 96 --height 192 --minibatch_size 64 --optimizer Adam
Stop-Transcript


#######################################################
# Below are configurations that already were 
# started on a machine and should not run again, 
# so we will terminate this PS-script here
# but retain those configurations for documentation
#######################################################
exit

# Started on Donkey, 08.06.2017, 12:00
Start-Transcript -path "$($pathToTranscript)2017-06-08_vgg_staff60-67-74-81_192x96_no_lr_reduction.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg -s 3 -offsets 60,67,74,81 --width 96 --height 192 --minibatch_size 64 --optimizer Adam --no_dynamic_learning_rate_reduction
Stop-Transcript

# Started on Donkey, 08.06.2017, 12:00
Start-Transcript -path "$($pathToTranscript)2017-06-08_vgg4_staff60-67-74-81_192x96_no_lr_reduction.txt" -append
python C:/Users/Alex/Repositories/MusicSymbolClassifier/HomusTrainer/TrainModel.py --model_name vgg4 -s 3 -offsets 60,67,74,81 --width 96 --height 192 --minibatch_size 64 --optimizer Adam --no_dynamic_learning_rate_reduction
Stop-Transcript