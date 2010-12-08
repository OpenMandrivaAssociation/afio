%define name afio
%define version 2.5
%define release %mkrel 7
%define summary Archiver program which writes cpio-format archives

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        %{summary}
Group:		Archiving/Backup
Source:		http://metalab.unc.edu/pub/linux/system/backup/%{name}-%{version}.tar.bz2
License:	LGPL
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
Afio makes cpio-format archives. It deals somewhat gracefully with input
data corruption, supports multi-volume archives during interactive
operation, and can make compressed archives that are much safer than
compressed tar or cpio archives. Afio is best used as an `archive engine'
in a backup script.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 afio $RPM_BUILD_ROOT%{_bindir}
install -m 755 afio.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc HISTORY INSTALLATION PORTING README SCRIPTS afio.lsm script1 script2 script3 script4
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
