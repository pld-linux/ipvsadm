Summary:	Utility to administer the Linux Virtual Server
Summary(pl):	Narz�dzie do administracji wirtualnymi serwerami
Name:		ipvsadm
Version:	1.21
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxvirtualserver.org/software/kernel-2.4/%{name}-%{version}.tar.gz
URL:		http://www.LinuxVirtualServer.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	popt-devel
Conflicts:	piranha <= 0.4.14
Conflicts:	kernel-headers < 2.4.17

%define		_sbindir	/sbin

%description
ipvsadm is a utility to administer the IP virtual server services
offered by the Linux kernel augmented with the virtual server patch.

%description -l pl
ipvsadm jest narz�dziem do administracji wirtualnymi serwerami,
mo�liwo�� taka dost�pna po spatchowaniu kernela patchem linux-ipvs

%prep
%setup -q

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}"


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install BUILD_ROOT=${RPM_BUILD_ROOT}

install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/ipvsadm
%{_mandir}/man?/ipvsadm.*
