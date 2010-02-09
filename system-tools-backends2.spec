%define oname system-tools-backends
Summary:	GNOME System Tools Backends
Name: 		system-tools-backends2
Version: 2.9.2
Release: %mkrel 1
License: 	GPLv2+ and LGPLv2+
Group: 		System/Configuration/Other
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2
Patch0:	system-tools-backends-2.8.1-mandriva.patch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
URL: 		http://www.gnome.org/projects/gst/
BuildRequires:	dbus-glib-devel
BuildRequires:	perl-Net-DBus
BuildRequires:	glib2-devel >= 2.15.2
BuildRequires:	polkit-1-devel
BuildRequires:	intltool
Requires:	polkit-agent
Conflicts:	system-tools-backends

%description
Day-to-day system management on Unix systems is a chore. Even when 
you're using a friendly graphical desktop, seemingly basic tasks 
like setting the system time, changing the network setup, importing 
and exporting network shared filesystems and configuring swap partitions 
requires editing configuration files by hand, and the exact procedure 
varies between different operating systems and distributions.

The GNOME System Tools solve all these problems, giving you a simple
graphical interface for each task, which uses an advanced backend to 
edit all the relevant files and apply your changes. The interface 
looks and acts in exactly the same way regardless of what platform 
you're using.

This package contains the backends of GNOME System Tools.

%prep
%setup -q -n %oname-%version

%build
#gw for backports, it has hardwired LOCALSTATEDIR/run as path
%define _localstatedir /var
%configure2_5x --with-stb-group=wheel
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std
mkdir -p %buildroot%_localstatedir/cache/%oname
%find_lang %oname

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -e %_initrddir/%oname ]; then
/sbin/service %oname stop > /dev/null ||:
/sbin/chkconfig --del %oname || :
fi

%files -f %oname.lang
%defattr(-, root, root)
%doc README AUTHORS NEWS 
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.freedesktop.SystemToolsBackends.conf
%_sbindir/%oname
%_datadir/dbus-1/system-services/org.freedesktop.SystemToolsBackends*.service
%_datadir/polkit-1/actions/org.freedesktop.SystemToolsBackends.policy
%_datadir/system-tools-backends-2.0/
%_libdir/pkgconfig/system-tools-backends-2.0.pc
%_localstatedir/cache/%oname


