%define name afio
%define version 2.5.1
%define release 1
%define summary Archiver program which writes cpio-format archives

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        %{summary}
Group:		Archiving/Backup
Source0:	http://members.chello.nl/~k.holtman/%{name}-%{version}.tgz
License:	LGPL

%description
Afio makes cpio-format archives. It deals somewhat gracefully with input
data corruption, supports multi-volume archives during interactive
operation, and can make compressed archives that are much safer than
compressed tar or cpio archives. Afio is best used as an `archive engine'
in a backup script.

%prep
%setup -q

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
