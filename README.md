# CoShare
<img width="50%" alt="icon" src="img/icon.png" class="center">

CoShare is a Screensharing-Tool to improve collaborative work.
This tool allows you to choose the shared region freely by your self
instead of sharing the entire screen or a single application.
As the receiving part, you can interact with the stream and even drag-and-drop file through it.
Content which is pasted in the clipboard is accessible for both parts.

## Install the application
1. Install GStreamer via `sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio`
2. Install xcopy as described here: https://www.chiark.greenend.org.uk/~sgtatham/utils/
2. Use `pip install -r requirements.txt` (or maybe `pip3`) to install the necessary packages.

## Run the application
1. If you are working with KDE, make sure to set the right window behaviour in system settings:
   - Force windows to be opened at top left corner to avoid inconsistent placement of transparent stream border:  
   Window Management -> Window Behavior -> Advanced -> Window placement: In Top-Left Corner
   - Avoid window movement by dragging the window to allow area choosing via drag gesture:  
   Application Style -> Configure style of your theme -> General -> Windows' drag mode: Drag windows from titlebar only
2. Add your user to group input. `usermod -a -G input {username}`
3. As the streaming part, make sure you have reading and writing permission for `/dev/uinput`.
To do this: `sudo chmod a+rw /dev/uinput`
4. Use `evtest` and `xinput` list to find out the event number of you keyboard and mouse device.
Make sure to use the mouse device which is listed as pointer **and** keyboard device.
5. Run `./extended_screenshare.sh` with `-k {your keyboard event number}` and `-m {your mouse event number}`

Make sure Streamer and Receiver are in the same network.

A tray icon appears. Use the option `Quit` to exit the application.
