---
title: "Windows VM Launcher"
date: 2017-12-25T08:22:40-05:00
draft: false
---

Create `~/.local/share/applications/windows.desktop` with the following content:
```
[Desktop Entry]
Version=1.0
Name=Windows 10
Comment=Starts the Windows 10 VM
Exec=bash -c 'virsh start Windows10 && virt-viewer --wait -c qemu:///system Windows10 && virsh shutdown Windows10'
Icon=windows
Type=Application
```
Under `Exec` change Windows10 to whatever you've named your VM.
After logging out and back in, you will now have Windows 10 as an "application" that you can run from your launcher (Unity or Gnome Shell or whatever it is).
If you shutdown the VM, the window will automatically close, and if you close the window without shutting down the VM, the Windows VM will safely shutdown in the background.
This saves you from having to go into virt-manager to start your VM - plus it's pretty slick.
