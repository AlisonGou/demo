#! /bin/bash
#this is a shell script to start python3 environment so arcpy in linux can be called. arcgis106 should be changed to the account to activate in your own environment.
su - arcgis106 <<EOF
echo 'going to set the ARCGISHOME value'
export ARCGISHOME=/home/arcgis106/arcgis/server
echo "going to activate environment"
source activate myenv
echo "going to execute python script"
python /home/convert.py
EOF
