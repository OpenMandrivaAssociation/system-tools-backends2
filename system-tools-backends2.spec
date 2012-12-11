%define oname system-tools-backends
Summary:	GNOME System Tools Backends
Name: 		system-tools-backends2
Version: 2.10.2
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




%changelog
* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 2.10.2-1mdv2011.0
+ Revision: 649886
- update to new version 2.10.2

* Sat Aug 21 2010 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdv2011.0
+ Revision: 571762
- update to new version 2.10.1

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.10.0-1mdv2010.1
+ Revision: 528907
- update to new version 2.10.0

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 2.9.4-1mdv2010.1
+ Revision: 516851
- update to new version 2.9.4

* Mon Feb 15 2010 Götz Waschk <waschk@mandriva.org> 2.9.3-1mdv2010.1
+ Revision: 506336
- update to new version 2.9.3

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 2.9.2-1mdv2010.1
+ Revision: 502711
- update to new version 2.9.2

* Sun Jan 17 2010 Götz Waschk <waschk@mandriva.org> 2.9.1-1mdv2010.1
+ Revision: 492866
- new version
- drop patches

* Fri Jan 15 2010 Götz Waschk <waschk@mandriva.org> 2.9.0-2mdv2010.1
+ Revision: 491818
- fix services names

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 2.9.0-1mdv2010.1
+ Revision: 489833
- update to new version 2.9.0

* Wed Dec 16 2009 Götz Waschk <waschk@mandriva.org> 2.8.3-1mdv2010.1
+ Revision: 479363
- update to new version 2.8.3

* Mon Oct 12 2009 Götz Waschk <waschk@mandriva.org> 2.8.2-1mdv2010.0
+ Revision: 456746
- new version

* Fri Sep 11 2009 Götz Waschk <waschk@mandriva.org> 2.8.1-3mdv2010.0
+ Revision: 438108
- conflict with old system-tools-backends

* Thu Aug 27 2009 Götz Waschk <waschk@mandriva.org> 2.8.1-2mdv2010.0
+ Revision: 421616
- update the patch
- remove initscript
- depend on polkit-agent

* Wed Aug 19 2009 Götz Waschk <waschk@mandriva.org> 2.8.1-1mdv2010.0
+ Revision: 418303
- new version
- drop merged patch

* Wed Aug 19 2009 Götz Waschk <waschk@mandriva.org> 2.8-1mdv2010.0
+ Revision: 418080
- new version
- drop patch 2
- patch for new binary location
- update deps for polkit-1
- update file list

* Wed Apr 15 2009 Götz Waschk <waschk@mandriva.org> 2.6.1-1mdv2009.1
+ Revision: 367523
- new version
- drop patch 1
- fix gettext package (b.g.o bug #579044)
- update file list
- fix installation
- add cache dir

* Fri Sep 12 2008 Götz Waschk <waschk@mandriva.org> 2.6.0-2mdv2009.0
+ Revision: 284069
- rediff patch for new mandriva versions
- fix build
- update license
- update build deps

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Sun Mar 09 2008 Götz Waschk <waschk@mandriva.org> 2.6.0-1mdv2008.1
+ Revision: 183039
- new version

* Wed Mar 05 2008 Götz Waschk <waschk@mandriva.org> 2.5.9-1mdv2008.1
+ Revision: 180146
- new version

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 2.5.8-1mdv2008.1
+ Revision: 165740
- new version

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 2.5.7-1mdv2008.1
+ Revision: 159413
- new version

* Tue Jan 15 2008 Götz Waschk <waschk@mandriva.org> 2.5.6-1mdv2008.1
+ Revision: 152174
- fix buildrequires
- new version
- new version
- update file list

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Götz Waschk <waschk@mandriva.org> 2.5.4-1mdv2008.1
+ Revision: 132038
- new version
- update file list

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 14 2007 Götz Waschk <waschk@mandriva.org> 2.5.3-1mdv2008.1
+ Revision: 108686
- new version

* Tue Oct 30 2007 Götz Waschk <waschk@mandriva.org> 2.5.1-1mdv2008.1
+ Revision: 103738
- new version

* Thu Oct 04 2007 Götz Waschk <waschk@mandriva.org> 2.4.1-1mdv2008.1
+ Revision: 95304
- new version

* Sat Sep 15 2007 Götz Waschk <waschk@mandriva.org> 2.4.0-1mdv2008.0
+ Revision: 85958
- new version

* Fri Sep 14 2007 Frederic Crozat <fcrozat@mandriva.com> 2.3.2-2mdv2008.0
+ Revision: 85510
- Update patch0 to detect 2008.0 correctly

* Tue Sep 04 2007 Götz Waschk <waschk@mandriva.org> 2.3.2-1mdv2008.0
+ Revision: 79026
- new version

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 2.3.1-1mdv2008.0
+ Revision: 72382
- new version

* Tue Jul 10 2007 Götz Waschk <waschk@mandriva.org> 2.3.0-1mdv2008.0
+ Revision: 50939
- new version

* Tue Jun 26 2007 Thierry Vignaud <tv@mandriva.org> 2.2.1-2mdv2008.0
+ Revision: 44535
- a service is not a config file

* Fri Apr 20 2007 Götz Waschk <waschk@mandriva.org> 2.2.1-1mdv2008.0
+ Revision: 16235
- rename service (bug #30339


* Wed Apr 04 2007 Götz Waschk <waschk@mandriva.org> 2.2.1-1mdv2007.1
+ Revision: 150473
- new version

* Fri Mar 16 2007 Götz Waschk <waschk@mandriva.org> 2.2.0-3mdv2007.1
+ Revision: 144897
- add initscript

* Fri Mar 16 2007 Götz Waschk <waschk@mandriva.org> 2.2.0-2mdv2007.1
+ Revision: 144884
- fix Mandriva patch

* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 2.2.0-1mdv2007.1
+ Revision: 141703
- new version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - no need to package big ChangeLog when NEWS is already there

* Thu Mar 01 2007 Götz Waschk <waschk@mandriva.org> 2.1.4-1mdv2007.1
+ Revision: 130310
- new version

* Tue Jan 23 2007 Götz Waschk <waschk@mandriva.org> 2.1.3-1mdv2007.1
+ Revision: 112293
- new version

* Tue Jan 09 2007 Götz Waschk <waschk@mandriva.org> 2.1.2-1mdv2007.1
+ Revision: 106365
- new version

* Mon Dec 04 2006 Götz Waschk <waschk@mandriva.org> 2.1.1-1mdv2007.1
+ Revision: 90317
- new version

* Fri Dec 01 2006 Götz Waschk <waschk@mandriva.org> 2.1.0-1mdv2007.1
+ Revision: 89554
- use the right configure macro
- fix installation on x86_64
- new version
- make it arch-dependant
- update build deps and file list
- unpack patch

* Sun Nov 26 2006 Götz Waschk <waschk@mandriva.org> 2.0.0-1mdv2007.1
+ Revision: 87342
- new version

* Sun Nov 05 2006 Götz Waschk <waschk@mandriva.org> 1.9.91-1mdv2007.1
+ Revision: 76761
- new version

* Fri Oct 27 2006 Götz Waschk <waschk@mandriva.org> 1.9.90-1mdv2007.1
+ Revision: 73042
- new version
- Import system-tools-backends2

* Sat Oct 07 2006 Götz Waschk <waschk@mandriva.org> 1.9.7-1mdv2007.1
- New version 1.9.7

* Sun Oct 01 2006 Götz Waschk <waschk@mandriva.org> 1.9.6-1mdv2007.0
- New version 1.9.6

* Wed Sep 13 2006 Götz Waschk <waschk@mandriva.org> 1.9.5.1-2mdv2007.0
- set stb group to wheel

* Tue Sep 12 2006 Götz Waschk <waschk@mandriva.org> 1.9.5.1-1mdv2007.0
- New version 1.9.5.1
- update file list

* Mon Aug 14 2006 Götz Waschk <waschk@mandriva.org> 1.9.3-1mdv2007.0
- New release 1.9.3

* Fri Aug 04 2006 Götz Waschk <waschk@mandriva.org> 1.9.2-1mdv2007.0
- initial package

