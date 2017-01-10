#
# spec file for package mysqldump-secure
#
# Copyright (c) 2017 stepping stone GmbH
#                    Switzerland
#                    http://www.stepping-stone.ch
#                    support@stepping-stone.ch
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public 
# License as published  by the Free Software Foundation, version
# 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License  along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
# Please submit enhancements, bugfixes or comments via GitHub:
# https://github.com/stepping-stone/centos-rpm-mysqldump-secure
#


Name:           mysqldump-secure
Version:        0.16.3
Release:        1%{?dist}
Summary:        APOSIX compliant wrapper script for mysqldump

License:        MIT
URL:            https://mysqldump-secure.org
Source0:        https://github.com/cytopia/%{name}/archive/%{version}.tar.gz
Patch0:         %{name}-destdirsupport.patch

BuildArch:      noarch

#BuildRequires:  
Requires:       mysql

%description
mysqldump-secure is a POSIX compliant wrapper script for mysqldump with
encryption capabilities and strong security in mind. It will backup every
available database (transaction-safe across tables) as a separate file with the
possibility to opt out via blacklisting. Dumped databases can optionally be
on-the-fly compressed (gzip, bzip2, xz, lzma, pigz, pbzip2, etc) as well as
encrypted with openssl assymetric encryption (no password needed). Compression
and encryption is done before the file is written to disk to avoid possible
race conditions.


%prep
%setup -q
%patch0


%build
# Currently the package only provides a self-styled limited configure script,
# so the configure macro can't be used.
./configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc
%{_sysconfdir}/*
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Tue Jan 10 2017 Christian Affolter <c.affolter@stepping-stone.ch> - 0.16.3-1
- Initial release

