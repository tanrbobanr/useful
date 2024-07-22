| TARGET | OBSERVING | PROBING | ATIME | MTIME | MODE | UID | GID | XATTRS | FLAGS |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `pd` | `cd` | chown |   |   |   |   |   |   |   |
| `pd` | `cf` | chown |   |   |   |   |   |   |   |
| `pd` | `cl` | chown |   |   |   |   |   |   | *?* |
| `pd` | `sd` | chown |   |   |   |   |   |   |   |
| `pd` | `sf` | chown |   |   |   |   |   |   |   |
| `pd` | `sl` | chown |   |   |   |   |   |   | *?* |
| `pd` | `pd` | tree/os.walk | **X** |   |   |   |   |   |   |
| `pd` | `cd` | tree/os.walk |   |   |   |   |   |   |   |
| `pd` | `cf` | tree/os.walk | **X** |   |   |   |   |   |   |
| `pd` | `cl` | tree/os.walk |   |   |   |   |   |   | *?* |
| `pd` | `sd` | tree/os.walk |   |   |   |   |   |   |   |
| `pd` | `sf` | tree/os.walk | **X** |   |   |   |   |   |   |
| `pd` | `sl` | tree/os.walk |   |   |   |   |   |   | *?* |
| `pd` | `pd` | ls/os.listdir |   |   |   |   |   |   |   |
| `pd` | `cd` | ls/os.listdir |   |   |   |   |   |   |   |
| `pd` | `cf` | ls/os.listdir |   |   |   |   |   |   |   |
| `pd` | `cl` | ls/os.listdir |   |   |   |   |   |   | *?* |
| `pd` | `sd` | ls/os.listdir |   |   |   |   |   |   |   |
| `pd` | `sf` | ls/os.listdir |   |   |   |   |   |   |   |
| `pd` | `sl` | ls/os.listdir |   |   |   |   |   |   | *?* |
| `pd` | `cd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `pd` | `cf` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `pd` | `cl` | touch -a -m/os.utime |   |   |   |   |   |   | *?* |
| `pd` | `sd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `pd` | `sf` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `pd` | `sl` | touch -a -m/os.utime |   |   |   |   |   |   | *?* |
| `pd` | `cd` | setfattr |   |   |   |   |   |   |   |
| `pd` | `cf` | setfattr |   |   |   |   |   |   |   |
| `pd` | `cl` | setfattr |   |   |   |   |   |   | *?* |
| `pd` | `sd` | setfattr |   |   |   |   |   |   |   |
| `pd` | `sf` | setfattr |   |   |   |   |   |   |   |
| `pd` | `sl` | setfattr |   |   |   |   |   |   | *?* |
| `pd` | `cd` | chattr |   |   |   |   |   |   |   |
| `pd` | `cf` | chattr |   |   |   |   |   |   |   |
| `pd` | `cl` | chattr |   |   |   |   |   |   | *?* |
| `pd` | `sd` | chattr |   |   |   |   |   |   |   |
| `pd` | `sf` | chattr |   |   |   |   |   |   |   |
| `pd` | `sl` | chattr |   |   |   |   |   |   | *?* |
| `cd` | `pd` | chown |   |   |   |   |   |   |   |
| `cd` | `cf` | chown |   |   |   |   |   |   |   |
| `cd` | `cl` | chown |   |   |   |   |   |   | *?* |
| `cd` | `pd` | tree/os.walk |   |   |   |   |   |   |   |
| `cd` | `cd` | tree/os.walk |   |   |   |   |   |   |   |
| `cd` | `cf` | tree/os.walk | **X** |   |   |   |   |   |   |
| `cd` | `cl` | tree/os.walk |   |   |   |   |   |   | *?* |
| `cd` | `sd` | tree/os.walk |   |   |   |   |   |   |   |
| `cd` | `sf` | tree/os.walk |   |   |   |   |   |   |   |
| `cd` | `sl` | tree/os.walk |   |   |   |   |   |   | *?* |
| `cd` | `pd` | ls/os.listdir |   |   |   |   |   |   |   |
| `cd` | `cd` | ls/os.listdir |   |   |   |   |   |   |   |
| `cd` | `cf` | ls/os.listdir |   |   |   |   |   |   |   |
| `cd` | `cl` | ls/os.listdir |   |   |   |   |   |   | *?* |
| `cd` | `sd` | ls/os.listdir |   |   |   |   |   |   |   |
| `cd` | `sf` | ls/os.listdir |   |   |   |   |   |   |   |
| `cd` | `sl` | ls/os.listdir |   |   |   |   |   |   | *?* |
| `cd` | `pd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `cd` | `cf` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `cd` | `cl` | touch -a -m/os.utime |   |   |   |   |   |   | *?* |
| `cd` | `pd` | setfattr |   |   |   |   |   |   |   |
| `cd` | `cf` | setfattr |   |   |   |   |   |   |   |
| `cd` | `cl` | setfattr |   |   |   |   |   |   | *?* |
| `cd` | `pd` | chattr |   |   |   |   |   |   |   |
| `cd` | `cf` | chattr |   |   |   |   |   |   |   |
| `cd` | `cl` | chattr |   |   |   |   |   |   | *?* |
| `cd` | `pd` | rmtree |   | **X** |   |   |   |   |   |
| `cd` | `cf` | rmtree |   |   |   |   |   |   |   |
| `cd` | `cl` | rmtree |   |   |   |   |   |   | *?* |
| `cd` | `pd` | mkdir |   | **X** |   |   |   |   |   |
| `cd` | `cf` | mkdir |   |   |   |   |   |   |   |
| `cd` | `cl` | mkdir |   |   |   |   |   |   | *?* |
| `cf` | `pd` | chown |   |   |   |   |   |   |   |
| `cf` | `cd` | chown |   |   |   |   |   |   |   |
| `cf` | `cl` | chown |   |   |   |   |   |   | *?* |
| `cf` | `sd` | chown |   |   |   |   |   |   |   |
| `cf` | `sf` | chown |   |   |   |   |   |   |   |
| `cf` | `sl` | chown |   |   |   |   |   |   | *?* |
| `cf` | `pd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `cf` | `cd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `cf` | `cl` | touch -a -m/os.utime |   |   |   |   |   |   | *?* |
| `cf` | `sd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `cf` | `sf` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `cf` | `sl` | touch -a -m/os.utime |   |   |   |   |   |   | *?* |
| `cf` | `pd` | setfattr |   |   |   |   |   |   |   |
| `cf` | `cd` | setfattr |   |   |   |   |   |   |   |
| `cf` | `cl` | setfattr |   |   |   |   |   |   | *?* |
| `cf` | `sd` | setfattr |   |   |   |   |   |   |   |
| `cf` | `sf` | setfattr |   |   |   |   |   |   |   |
| `cf` | `sl` | setfattr |   |   |   |   |   |   | *?* |
| `cf` | `pd` | chattr |   |   |   |   |   |   |   |
| `cf` | `cd` | chattr |   |   |   |   |   |   |   |
| `cf` | `cl` | chattr |   |   |   |   |   |   | *?* |
| `cf` | `sd` | chattr |   |   |   |   |   |   |   |
| `cf` | `sf` | chattr |   |   |   |   |   |   |   |
| `cf` | `sl` | chattr |   |   |   |   |   |   | *?* |
| `cf` | `pd` | open (r) |   |   |   |   |   |   |   |
| `cf` | `cd` | open (r) |   |   |   |   |   |   |   |
| `cf` | `cf` | open (r) |   |   |   |   |   |   |   |
| `cf` | `cl` | open (r) |   |   |   |   |   |   | *?* |
| `cf` | `sd` | open (r) |   |   |   |   |   |   |   |
| `cf` | `sf` | open (r) |   |   |   |   |   |   |   |
| `cf` | `sl` | open (r) |   |   |   |   |   |   | *?* |
| `cf` | `pd` | open (r) & read |   |   |   |   |   |   |   |
| `cf` | `cd` | open (r) & read | **X** |   |   |   |   |   |   |
| `cf` | `cf` | open (r) & read |   |   |   |   |   |   |   |
| `cf` | `cl` | open (r) & read |   |   |   |   |   |   | *?* |
| `cf` | `sd` | open (r) & read |   |   |   |   |   |   |   |
| `cf` | `sf` | open (r) & read |   |   |   |   |   |   |   |
| `cf` | `sl` | open (r) & read |   |   |   |   |   |   | *?* |
| `cf` | `pd` | open (w) |   |   |   |   |   |   |   |
| `cf` | `cd` | open (w) |   | **X** |   |   |   |   |   |
| `cf` | `cf` | open (w) |   |   |   |   |   |   |   |
| `cf` | `cl` | open (w) |   |   |   |   |   |   | *?* |
| `cf` | `sd` | open (w) |   |   |   |   |   |   |   |
| `cf` | `sf` | open (w) |   |   |   |   |   |   |   |
| `cf` | `sl` | open (w) |   |   |   |   |   |   | *?* |
| `cf` | `pd` | open (w) & write |   |   |   |   |   |   |   |
| `cf` | `cd` | open (w) & write |   | **X** |   |   |   |   |   |
| `cf` | `cf` | open (w) & write |   |   |   |   |   |   |   |
| `cf` | `cl` | open (w) & write |   |   |   |   |   |   | *?* |
| `cf` | `sd` | open (w) & write |   |   |   |   |   |   |   |
| `cf` | `sf` | open (w) & write |   |   |   |   |   |   |   |
| `cf` | `sl` | open (w) & write |   |   |   |   |   |   | *?* |
| `cf` | `pd` | unlink |   | **X** |   |   |   |   |   |
| `cf` | `cd` | unlink |   |   |   |   |   |   |   |
| `cf` | `cl` | unlink |   |   |   |   |   |   | *?* |
| `cf` | `sd` | unlink |   |   |   |   |   |   |   |
| `cf` | `sf` | unlink |   |   |   |   |   |   |   |
| `cf` | `sl` | unlink |   |   |   |   |   |   | *?* |
| `cf` | `pd` | touch |   | **X** |   |   |   |   |   |
| `cf` | `cd` | touch |   |   |   |   |   |   |   |
| `cf` | `cl` | touch |   |   |   |   |   |   | *?* |
| `cf` | `sd` | touch |   |   |   |   |   |   |   |
| `cf` | `sf` | touch |   |   |   |   |   |   |   |
| `cf` | `sl` | touch |   |   |   |   |   |   | *?* |
| `cl` | `pd` | chown |   |   |   |   |   |   |   |
| `cl` | `cd` | chown |   |   |   | **X** | **X** |   |   |
| `cl` | `cf` | chown |   |   |   |   |   |   |   |
| `cl` | `sd` | chown |   |   |   |   |   |   |   |
| `cl` | `sf` | chown |   |   |   |   |   |   |   |
| `cl` | `sl` | chown |   |   |   |   |   |   | *?* |
| `cl` | `pd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `cl` | `cd` | touch -a -m/os.utime | **X** | **X** |   |   |   |   |   |
| `cl` | `cf` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `cl` | `sd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `cl` | `sf` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `cl` | `sl` | touch -a -m/os.utime |   |   |   |   |   |   | *?* |
| `cl` | `pd` | setfattr |   |   |   |   |   |   |   |
| `cl` | `cd` | setfattr |   |   |   |   |   |   |   |
| `cl` | `cf` | setfattr |   |   |   |   |   |   |   |
| `cl` | `sd` | setfattr |   |   |   |   |   |   |   |
| `cl` | `sf` | setfattr |   |   |   |   |   |   |   |
| `cl` | `sl` | setfattr |   |   |   |   |   |   | *?* |
| `cl` | `pd` | chattr |   |   |   |   |   |   |   |
| `cl` | `cd` | chattr |   |   |   |   |   |   |   |
| `cl` | `cf` | chattr |   |   |   |   |   |   |   |
| `cl` | `sd` | chattr |   |   |   |   |   |   |   |
| `cl` | `sf` | chattr |   |   |   |   |   |   |   |
| `cl` | `sl` | chattr |   |   |   |   |   |   | *?* |
| `cl` | `pd` | open (r) |   |   |   |   |   |   |   |
| `cl` | `cd` | open (r) |   |   |   |   |   |   |   |
| `cl` | `cf` | open (r) |   |   |   |   |   |   |   |
| `cl` | `cl` | open (r) |   |   |   |   |   |   | *?* |
| `cl` | `sd` | open (r) |   |   |   |   |   |   |   |
| `cl` | `sf` | open (r) |   |   |   |   |   |   |   |
| `cl` | `sl` | open (r) |   |   |   |   |   |   | *?* |
| `cl` | `pd` | open (r) & read |   |   |   |   |   |   |   |
| `cl` | `cd` | open (r) & read | **X** |   |   |   |   |   |   |
| `cl` | `cf` | open (r) & read |   |   |   |   |   |   |   |
| `cl` | `cl` | open (r) & read |   |   |   |   |   |   | *?* |
| `cl` | `sd` | open (r) & read |   |   |   |   |   |   |   |
| `cl` | `sf` | open (r) & read |   |   |   |   |   |   |   |
| `cl` | `sl` | open (r) & read |   |   |   |   |   |   | *?* |
| `cl` | `pd` | open (w) |   |   |   |   |   |   |   |
| `cl` | `cd` | open (w) |   | **X** |   |   |   |   |   |
| `cl` | `cf` | open (w) |   |   |   |   |   |   |   |
| `cl` | `cl` | open (w) |   |   |   |   |   |   | *?* |
| `cl` | `sd` | open (w) |   |   |   |   |   |   |   |
| `cl` | `sf` | open (w) |   |   |   |   |   |   |   |
| `cl` | `sl` | open (w) |   |   |   |   |   |   | *?* |
| `cl` | `pd` | open (w) & write |   |   |   |   |   |   |   |
| `cl` | `cd` | open (w) & write |   | **X** |   |   |   |   |   |
| `cl` | `cf` | open (w) & write |   |   |   |   |   |   |   |
| `cl` | `cl` | open (w) & write |   |   |   |   |   |   | *?* |
| `cl` | `sd` | open (w) & write |   |   |   |   |   |   |   |
| `cl` | `sf` | open (w) & write |   |   |   |   |   |   |   |
| `cl` | `sl` | open (w) & write |   |   |   |   |   |   | *?* |
| `cl` | `pd` | unlink |   | **X** |   |   |   |   |   |
| `cl` | `cd` | unlink |   |   |   |   |   |   |   |
| `cl` | `cf` | unlink |   |   |   |   |   |   |   |
| `cl` | `sd` | unlink |   |   |   |   |   |   |   |
| `cl` | `sf` | unlink |   |   |   |   |   |   |   |
| `cl` | `sl` | unlink |   |   |   |   |   |   | *?* |
| `cl` | `pd` | ls -s |   | **X** |   |   |   |   |   |
| `cl` | `cd` | ls -s |   |   |   |   |   |   |   |
| `cl` | `cf` | ls -s |   |   |   |   |   |   |   |
| `cl` | `sd` | ls -s |   |   |   |   |   |   |   |
| `cl` | `sf` | ls -s |   |   |   |   |   |   |   |
| `cl` | `sl` | ls -s |   |   |   |   |   |   | *?* |
| `sd` | `pd` | chown |   |   |   |   |   |   |   |
| `sd` | `cd` | chown |   |   |   |   |   |   |   |
| `sd` | `cf` | chown |   |   |   |   |   |   |   |
| `sd` | `cl` | chown |   |   |   |   |   |   | *?* |
| `sd` | `sf` | chown |   |   |   |   |   |   |   |
| `sd` | `sl` | chown |   |   |   |   |   |   | *?* |
| `sd` | `pd` | tree/os.walk |   |   |   |   |   |   |   |
| `sd` | `cd` | tree/os.walk |   |   |   |   |   |   |   |
| `sd` | `cf` | tree/os.walk |   |   |   |   |   |   |   |
| `sd` | `cl` | tree/os.walk |   |   |   |   |   |   | *?* |
| `sd` | `sd` | tree/os.walk |   |   |   |   |   |   |   |
| `sd` | `sf` | tree/os.walk | **X** |   |   |   |   |   |   |
| `sd` | `sl` | tree/os.walk |   |   |   |   |   |   | *?* |
| `sd` | `pd` | ls/os.listdir |   |   |   |   |   |   |   |
| `sd` | `cd` | ls/os.listdir |   |   |   |   |   |   |   |
| `sd` | `cf` | ls/os.listdir |   |   |   |   |   |   |   |
| `sd` | `cl` | ls/os.listdir |   |   |   |   |   |   | *?* |
| `sd` | `sd` | ls/os.listdir |   |   |   |   |   |   |   |
| `sd` | `sf` | ls/os.listdir |   |   |   |   |   |   |   |
| `sd` | `sl` | ls/os.listdir |   |   |   |   |   |   | *?* |
| `sd` | `pd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sd` | `cd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sd` | `cf` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sd` | `cl` | touch -a -m/os.utime |   |   |   |   |   |   | *?* |
| `sd` | `sf` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sd` | `sl` | touch -a -m/os.utime |   |   |   |   |   |   | *?* |
| `sd` | `pd` | setfattr |   |   |   |   |   |   |   |
| `sd` | `cd` | setfattr |   |   |   |   |   |   |   |
| `sd` | `cf` | setfattr |   |   |   |   |   |   |   |
| `sd` | `cl` | setfattr |   |   |   |   |   |   | *?* |
| `sd` | `sf` | setfattr |   |   |   |   |   |   |   |
| `sd` | `sl` | setfattr |   |   |   |   |   |   | *?* |
| `sd` | `pd` | chattr |   |   |   |   |   |   |   |
| `sd` | `cd` | chattr |   |   |   |   |   |   |   |
| `sd` | `cf` | chattr |   |   |   |   |   |   |   |
| `sd` | `cl` | chattr |   |   |   |   |   |   | *?* |
| `sd` | `sf` | chattr |   |   |   |   |   |   |   |
| `sd` | `sl` | chattr |   |   |   |   |   |   | *?* |
| `sd` | `pd` | rmdir |   |   |   |   |   |   |   |
| `sd` | `cd` | rmdir |   |   |   |   |   |   |   |
| `sd` | `cf` | rmdir |   | **X** |   |   |   |   |   |
| `sd` | `cl` | rmdir |   |   |   |   |   |   | *?* |
| `sd` | `sf` | rmdir |   |   |   |   |   |   |   |
| `sd` | `sl` | rmdir |   |   |   |   |   |   | *?* |
| `sd` | `pd` | rmtree |   |   |   |   |   |   |   |
| `sd` | `cd` | rmtree |   |   |   |   |   |   |   |
| `sd` | `cf` | rmtree |   | **X** |   |   |   |   |   |
| `sd` | `cl` | rmtree |   |   |   |   |   |   | *?* |
| `sd` | `sf` | rmtree |   |   |   |   |   |   |   |
| `sd` | `sl` | rmtree |   |   |   |   |   |   | *?* |
| `sd` | `pd` | mkdir |   |   |   |   |   |   |   |
| `sd` | `cd` | mkdir |   |   |   |   |   |   |   |
| `sd` | `cf` | mkdir |   | **X** |   |   |   |   |   |
| `sd` | `cl` | mkdir |   |   |   |   |   |   | *?* |
| `sd` | `sf` | mkdir |   |   |   |   |   |   |   |
| `sd` | `sl` | mkdir |   |   |   |   |   |   | *?* |
| `sf` | `pd` | chown |   |   |   |   |   |   |   |
| `sf` | `cd` | chown |   |   |   |   |   |   |   |
| `sf` | `cf` | chown |   |   |   |   |   |   |   |
| `sf` | `cl` | chown |   |   |   |   |   |   | *?* |
| `sf` | `sd` | chown |   |   |   |   |   |   |   |
| `sf` | `sl` | chown |   |   |   |   |   |   | *?* |
| `sf` | `pd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sf` | `cd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sf` | `cf` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sf` | `cl` | touch -a -m/os.utime |   |   |   |   |   |   | *?* |
| `sf` | `sd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sf` | `sl` | touch -a -m/os.utime |   |   |   |   |   |   | *?* |
| `sf` | `pd` | setfattr |   |   |   |   |   |   |   |
| `sf` | `cd` | setfattr |   |   |   |   |   |   |   |
| `sf` | `cf` | setfattr |   |   |   |   |   |   |   |
| `sf` | `cl` | setfattr |   |   |   |   |   |   | *?* |
| `sf` | `sd` | setfattr |   |   |   |   |   |   |   |
| `sf` | `sl` | setfattr |   |   |   |   |   |   | *?* |
| `sf` | `pd` | chattr |   |   |   |   |   |   |   |
| `sf` | `cd` | chattr |   |   |   |   |   |   |   |
| `sf` | `cf` | chattr |   |   |   |   |   |   |   |
| `sf` | `cl` | chattr |   |   |   |   |   |   | *?* |
| `sf` | `sd` | chattr |   |   |   |   |   |   |   |
| `sf` | `sl` | chattr |   |   |   |   |   |   | *?* |
| `sf` | `pd` | open (r) |   |   |   |   |   |   |   |
| `sf` | `cd` | open (r) |   |   |   |   |   |   |   |
| `sf` | `cf` | open (r) |   |   |   |   |   |   |   |
| `sf` | `cl` | open (r) |   |   |   |   |   |   | *?* |
| `sf` | `sd` | open (r) |   |   |   |   |   |   |   |
| `sf` | `sf` | open (r) |   |   |   |   |   |   |   |
| `sf` | `sl` | open (r) |   |   |   |   |   |   | *?* |
| `sf` | `pd` | open (r) & read |   |   |   |   |   |   |   |
| `sf` | `cd` | open (r) & read |   |   |   |   |   |   |   |
| `sf` | `cf` | open (r) & read |   |   |   |   |   |   |   |
| `sf` | `cl` | open (r) & read |   |   |   |   |   |   | *?* |
| `sf` | `sd` | open (r) & read | **X** |   |   |   |   |   |   |
| `sf` | `sf` | open (r) & read |   |   |   |   |   |   |   |
| `sf` | `sl` | open (r) & read |   |   |   |   |   |   | *?* |
| `sf` | `pd` | open (w) |   |   |   |   |   |   |   |
| `sf` | `cd` | open (w) |   |   |   |   |   |   |   |
| `sf` | `cf` | open (w) |   |   |   |   |   |   |   |
| `sf` | `cl` | open (w) |   |   |   |   |   |   | *?* |
| `sf` | `sd` | open (w) |   | **X** |   |   |   |   |   |
| `sf` | `sf` | open (w) |   |   |   |   |   |   |   |
| `sf` | `sl` | open (w) |   |   |   |   |   |   | *?* |
| `sf` | `pd` | open (w) & write |   |   |   |   |   |   |   |
| `sf` | `cd` | open (w) & write |   |   |   |   |   |   |   |
| `sf` | `cf` | open (w) & write |   |   |   |   |   |   |   |
| `sf` | `cl` | open (w) & write |   |   |   |   |   |   | *?* |
| `sf` | `sd` | open (w) & write |   | **X** |   |   |   |   |   |
| `sf` | `sf` | open (w) & write |   |   |   |   |   |   |   |
| `sf` | `sl` | open (w) & write |   |   |   |   |   |   | *?* |
| `sf` | `pd` | unlink |   |   |   |   |   |   |   |
| `sf` | `cd` | unlink |   |   |   |   |   |   |   |
| `sf` | `cf` | unlink |   | **X** |   |   |   |   |   |
| `sf` | `cl` | unlink |   |   |   |   |   |   | *?* |
| `sf` | `sd` | unlink |   |   |   |   |   |   |   |
| `sf` | `sl` | unlink |   |   |   |   |   |   | *?* |
| `sf` | `pd` | touch |   |   |   |   |   |   |   |
| `sf` | `cd` | touch |   |   |   |   |   |   |   |
| `sf` | `cf` | touch |   | **X** |   |   |   |   |   |
| `sf` | `cl` | touch |   |   |   |   |   |   | *?* |
| `sf` | `sd` | touch |   |   |   |   |   |   |   |
| `sf` | `sl` | touch |   |   |   |   |   |   | *?* |
| `sl` | `pd` | chown |   |   |   |   |   |   |   |
| `sl` | `cd` | chown |   |   |   |   |   |   |   |
| `sl` | `cf` | chown |   |   |   |   |   |   |   |
| `sl` | `cl` | chown |   |   |   |   |   |   | *?* |
| `sl` | `sd` | chown |   |   |   | **X** | **X** |   |   |
| `sl` | `sf` | chown |   |   |   |   |   |   |   |
| `sl` | `pd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sl` | `cd` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sl` | `cf` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sl` | `cl` | touch -a -m/os.utime |   |   |   |   |   |   | *?* |
| `sl` | `sd` | touch -a -m/os.utime | **X** | **X** |   |   |   |   |   |
| `sl` | `sf` | touch -a -m/os.utime |   |   |   |   |   |   |   |
| `sl` | `pd` | setfattr |   |   |   |   |   |   |   |
| `sl` | `cd` | setfattr |   |   |   |   |   |   |   |
| `sl` | `cf` | setfattr |   |   |   |   |   |   |   |
| `sl` | `cl` | setfattr |   |   |   |   |   |   | *?* |
| `sl` | `sd` | setfattr |   |   |   |   |   |   |   |
| `sl` | `sf` | setfattr |   |   |   |   |   |   |   |
| `sl` | `pd` | chattr |   |   |   |   |   |   |   |
| `sl` | `cd` | chattr |   |   |   |   |   |   |   |
| `sl` | `cf` | chattr |   |   |   |   |   |   |   |
| `sl` | `cl` | chattr |   |   |   |   |   |   | *?* |
| `sl` | `sd` | chattr |   |   |   |   |   |   |   |
| `sl` | `sf` | chattr |   |   |   |   |   |   |   |
| `sl` | `pd` | open (r) |   |   |   |   |   |   |   |
| `sl` | `cd` | open (r) |   |   |   |   |   |   |   |
| `sl` | `cf` | open (r) |   |   |   |   |   |   |   |
| `sl` | `cl` | open (r) |   |   |   |   |   |   | *?* |
| `sl` | `sd` | open (r) |   |   |   |   |   |   |   |
| `sl` | `sf` | open (r) |   |   |   |   |   |   |   |
| `sl` | `sl` | open (r) |   |   |   |   |   |   | *?* |
| `sl` | `pd` | open (r) & read |   |   |   |   |   |   |   |
| `sl` | `cd` | open (r) & read |   |   |   |   |   |   |   |
| `sl` | `cf` | open (r) & read |   |   |   |   |   |   |   |
| `sl` | `cl` | open (r) & read |   |   |   |   |   |   | *?* |
| `sl` | `sd` | open (r) & read | **X** |   |   |   |   |   |   |
| `sl` | `sf` | open (r) & read |   |   |   |   |   |   |   |
| `sl` | `sl` | open (r) & read |   |   |   |   |   |   | *?* |
| `sl` | `pd` | open (w) |   |   |   |   |   |   |   |
| `sl` | `cd` | open (w) |   |   |   |   |   |   |   |
| `sl` | `cf` | open (w) |   |   |   |   |   |   |   |
| `sl` | `cl` | open (w) |   |   |   |   |   |   | *?* |
| `sl` | `sd` | open (w) |   | **X** |   |   |   |   |   |
| `sl` | `sf` | open (w) |   |   |   |   |   |   |   |
| `sl` | `sl` | open (w) |   |   |   |   |   |   | *?* |
| `sl` | `pd` | open (w) & write |   |   |   |   |   |   |   |
| `sl` | `cd` | open (w) & write |   |   |   |   |   |   |   |
| `sl` | `cf` | open (w) & write |   |   |   |   |   |   |   |
| `sl` | `cl` | open (w) & write |   |   |   |   |   |   | *?* |
| `sl` | `sd` | open (w) & write |   | **X** |   |   |   |   |   |
| `sl` | `sf` | open (w) & write |   |   |   |   |   |   |   |
| `sl` | `sl` | open (w) & write |   |   |   |   |   |   | *?* |
| `sl` | `pd` | unlink |   |   |   |   |   |   |   |
| `sl` | `cd` | unlink |   |   |   |   |   |   |   |
| `sl` | `cf` | unlink |   | **X** |   |   |   |   |   |
| `sl` | `cl` | unlink |   |   |   |   |   |   | *?* |
| `sl` | `sd` | unlink |   |   |   |   |   |   |   |
| `sl` | `sf` | unlink |   |   |   |   |   |   |   |
| `sl` | `pd` | ls -s |   |   |   |   |   |   |   |
| `sl` | `cd` | ls -s |   |   |   |   |   |   |   |
| `sl` | `cf` | ls -s |   | **X** |   |   |   |   |   |
| `sl` | `cl` | ls -s |   |   |   |   |   |   | *?* |
| `sl` | `sd` | ls -s |   |   |   |   |   |   |   |
| `sl` | `sf` | ls -s |   |   |   |   |   |   |   |
