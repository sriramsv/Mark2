import dbus
item              = "org.freedesktop.Notifications"
path              = "/org/freedesktop/Notifications"
interface         = "org.freedesktop.Notifications"
app_name          = "Test Application"
id_num_to_replace = 0
icon              = "/usr/share/icons/Tango/32x32/status/sunny.png"
title             = "Notification Title"
text              = "This is the body"
actions_list      = ''
hint              = ''
time              = 1   # Use seconds x 1000

bus = dbus.SessionBus()
notif = bus.get_object(item, path)
notify = dbus.Interface(notif, interface)
notify.Notify(app_name, id_num_to_replace, icon, title, text, actions_list, hint, time)
