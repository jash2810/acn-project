INPUT_DIR=inputs
OUTPUT_DIR=results
INPUT_FILES='pingdata'
DURATION=50

for f in $INPUT_FILES;
do
        input_file=$INPUT_DIR/$f
        pref="iperf"
        out_dir=$OUTPUT_DIR/$pref/$f
        sudo python2.7 mininet_script.py -i $input_file -d $out_dir -p 0.03 -t $DURATION --dij --iperf
done
sudo python2.7 clean.py
firefox results/data.html
sudo mn -c
