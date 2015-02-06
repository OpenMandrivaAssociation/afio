%define name afio
%define version 2.5.1
%define release 2
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


%changelog
* Sun Mar 11 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.5.1-1
+ Revision: 784257
- version update 2.5.1

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5-7mdv2011.0
+ Revision: 616503
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 2.5-6mdv2010.0
+ Revision: 436632
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.5-5mdv2009.1
+ Revision: 350725
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 2.5-4mdv2009.0
+ Revision: 226133
- rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 2.5-3mdv2008.1
+ Revision: 135819
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Bruno Cornec <bcornec@mandriva.org> 2.5-3mdv2008.0
+ Revision: 77246
- Import afio

