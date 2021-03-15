
<p align="center" width="100%">
    <img width="33%" src="https://user-images.githubusercontent.com/56304060/111104618-14b5e700-8577-11eb-8d28-a3348d1a4dcf.jpg" alt="ezBeat❤"> 
</p>



# EasyBeat 

A **webapp** that takes patients ECG readings from their wearable devices and uses a LSTM-based-Autoencoder to detect if there is an anomaly in their heart readings. If the data is abnormal, our tool will send the important data to the patient's electronic medical records and provide them with a simple “normal” vs “abnormal” result.


# How to use it ?

* Install [python 3.7+](https://www.python.org/downloads/release/python-378/)
* Open a terminal and type in the below command to install **virtualenv** module
~~~
pip install virtualenv
~~~

* Create a new folder and clone this repository *(Assuming you have already have **git** installed)*
~~~
git clone https://github.com/HOTSONHONET/eazyBeat.git
~~~

* Use `Shift + rightclick` to open up a terminal in the folder
* Create a virtual environment and install all the dependecies from **requirements.txt**
~~~
virtualenv <name-of-env>
./<name-of-env>/Scripts/activate
pip install -r requirements.txt
~~~
* Now, once all of the packages are installed, go to the cloned folder and run this command to start the application *(Assuming you are on windows like me 😉, for linux and mac use **python3** instead of **py**)*
~~~
cd ./main
py wsgi.py
~~~

* You will see a **http** url in the terminal, copy that link and open it in your browser

# Working images

<table>
  <tr>
    <td>Terminal</td>
     <td>Homepage</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/56304060/111106029-4c725e00-857a-11eb-8ca3-35259b4e84c0.png" width=500 height=200></td>
    <td><img src="https://user-images.githubusercontent.com/56304060/111106086-64e27880-857a-11eb-8158-1937308fdc40.png" width=500 height=200></td>
  </tr>
  <tr>
    <td>About</td>
     <td>Uploading the form</td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/56304060/111106089-67dd6900-857a-11eb-9cc9-c2058a474d6a.png" width=500 height=200></td>
    <td><img src="https://user-images.githubusercontent.com/56304060/111106107-7166d100-857a-11eb-839f-72583c91f9ad.png" width=500 height=200></td>
    
  </tr>
 <tr>
    <td>Showing Normal ECG</td>
     <td>Model prediction</td>
  </tr>
  <tr>    
    <td><img src="https://user-images.githubusercontent.com/56304060/111106116-73c92b00-857a-11eb-847b-b9f273f5a10f.png" width=500 height=200></td>
    <td><img src="https://user-images.githubusercontent.com/56304060/111106120-7592ee80-857a-11eb-8fd9-ed2ff9a43fee.png" width=500 height=200></td>
  </tr>
 </table>



