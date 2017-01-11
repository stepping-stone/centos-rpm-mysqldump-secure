# centos-rpm-mysqldump-secure
CentOS 7 RPM Specfile for [mysqldump-secure](https://mysqldump-secure.org/) which is part of [stepping stone GmbH's CentOS package collection](https://build.opensuse.org/project/show/home:stepping-stone:sst-centos).

## Usage
There are pre-built binary packages for CentOS 7 available on [stepping stone GmbH's CentOS package repository](https://build.opensuse.org/project/show/home:stepping-stone:sst-centos), which can be installed as follows:

```bash
curl -o /etc/yum.repos.d/home:stepping-stone:sst-centos.repo \
     http://download.opensuse.org/repositories/home:/stepping-stone:/sst-centos/CentOS_7/home:stepping-stone:sst-centos.repo
     
yum install mysqldump-secure
```

### Configuration
[Configure](https://mysqldump-secure.org/documentation/configuration.php) the MySQL/MariaDB credentials and mysqldump-secure options:
```bash
vi /etc/mysqldump-secure.cnf
vi /etc/mysqldump-secure.conf
```

### Running mysqldump-secure through systemd
There's a systemd timer unit available which runs mysqldump-secure once per day at midnight [<code>OnCalendar=daily</code>](https://www.freedesktop.org/software/systemd/man/systemd.time.html#Calendar%20Events) per default. To enable it:

```bash
systemctl enable mysqldump-secure.timer
systemctl start mysqldump-secure.timer

systemctl list-timers
```

In case you might want to change the start time, override the [<code>OnCalendar</code>](https://www.freedesktop.org/software/systemd/man/systemd.timer.html#OnCalendar=) directive:
```bash
systemctl edit mysqldump-secure.timer
```

```INI
[Timer]
OnCalendar=*-*-* HH:MM:SS
```
