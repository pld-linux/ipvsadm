%define prefix   /usr

Summary:	Utility to administer the Linux Virtual Server
Summary(pl):	Narzêdzie do administracji wirtualnymi serwerami
Name:		ipvsadm
Version:	1.14
Release:	1
Copyright:	GNU General Public Licence
URL:		http://www.LinuxVirtualServer.org/
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0: 	http://www.linuxvirtualserver.org/software/ipvsadm-1.14.tar.gz	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	%{name}-%{version}
Obsoletes:	ipvsadm <= 1.10

%description
ipvsadm is a utility to administer the IP virtual server services
offered by the Linux kernel augmented with the virtual server patch.

%description -l pl
ipvsadm jest narzêdziem do administracji wirtualnymi serwerami,
mo¿liwo¶æ taka dostêpna po spatchowaniu kernela patchem linux-ipvs

%prep
%setup -q -n ipvsadm


%build
CFLAGS="${RPM_OPT_FLAGS}" make


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install *.8 $RPM_BUILD_ROOT%{_mandir}/man8
BUILD_ROOT=${RPM_BUILD_ROOT} make install

#File finding code thanks to Samuel Flory of VA Linux Systems
cd ${RPM_BUILD_ROOT}
# Directories
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' \
  > ${RPM_BUILD_DIR}/%{name}-%{version}-%{release}.files
# Files
find . -type f | sed "s,^\.\(.*\),%attr (-\,root\,root) \1*," \
  >> ${RPM_BUILD_DIR}/%{name}-%{version}-%{release}.files
# Symbolic links
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' \
  >> ${RPM_BUILD_DIR}/%{name}-%{version}-%{release}.files


%clean
rm -rf $RPM_BUILD_DIR/%{name}
rm -rf $RPM_BUILD_ROOT
rm -f ${RPM_BUILD_DIR}/%{name}-%{version}-%{release}.files

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %{_sbindir}/ipvsadm
%{_mandir}/man8/ipvsadm.8*
%doc README
