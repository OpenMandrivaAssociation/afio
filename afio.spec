#define debug_package	%{nil}

Name:           afio
Version:        2.5.2
Release:        1
Summary:        Archiver program which writes cpio format archives
Group:		Archiving/Backup
Url:		https://members.chello.nl/~k.holtman/afio.html
Source0:	https://fossies.org/linux/misc/afio-%{version}.tar.xz
License:	LGPL

%description
Afio makes cpio-format archives. It deals somewhat gracefully with input
data corruption, supports multi-volume archives during interactive
operation, and can make compressed archives that are much safer than
compressed tar or cpio archives. Afio is best used as an `archive engine'
in a backup script.

%prep
%setup -q
chmod 644 script3/my_passphrasefile

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 afio %{buildroot}%{_bindir}
install -m 755 afio.1 %{buildroot}%{_mandir}/man1


%files
%doc HISTORY INSTALLATION PORTING README SCRIPTS afio.lsm script1 script2 script3 script4
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


