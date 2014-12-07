%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		wildmidi
Version:	0.2.3.5
Release:	11
Summary:	Open Source Midi Sequencer
Group:		Sound
License:	GPLv3+ and LGPLv3+
URL:		http://wildmidi.sourceforge.net
Source:		http://dfn.dl.sourceforge.net/sourceforge/wildmidi/%name-%version.tar.gz
Patch0:		wildmidi-0.2.3.4-fix-default-config-location.patch
BuildRequires:	timidity-instruments
BuildRequires:	pkgconfig(alsa)
Requires:	timidity-instruments

%description
WildMidi is a software midi play which has a core softsynth
library that can be use with other applications.

%files
%doc docs/*v3.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.cfg.5*

#------------------------------------------------------------------------------------------------
%package -n %{libname}
Summary: Library for wildmidi
Group: System/Libraries

%description -n %{libname}
This package contains library files for wildmidi

%files -n %{libname}
%{_libdir}/*.so.%{major}*

#------------------------------------------------------------------------------------------------
%package -n %{develname}
Summary:	Development files for wildmidi
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains development files for wildmidi

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*.h
%{_mandir}/man3/*.3*

#------------------------------------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0 -b .defconfig

%build
%configure2_5x --disable-static \
		--without-arch \
		--disable-werror

# parallel build fails, so we don't use it
make

%install
%makeinstall_std



%changelog
* Sat Aug 18 2012 Andrey Bondrov <abondrov@mandriva.org> 0.2.3.5-2
+ Revision: 815309
- Update files
- Don't use parallel build as it fails
- New version 0.2.3.5, spec cleanup

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 0.2.3.4-1mdv2011.0
+ Revision: 563742
- new version 0.2.3.4

* Sun Jul 11 2010 Emmanuel Andry <eandry@mandriva.org> 0.2.3.3-1mdv2011.0
+ Revision: 550959
- New version 0.2.3.3
- New major 1
- drop p0, p1, p2
- rediff p3
- update files list

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.2.2-7mdv2010.0
+ Revision: 445782
- rebuild

* Wed Feb 25 2009 Götz Waschk <waschk@mandriva.org> 0.2.2-6mdv2009.1
+ Revision: 344624
- update license

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.2.2-6mdv2009.0
+ Revision: 269681
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 14 2008 Funda Wang <fwang@mandriva.org> 0.2.2-5mdv2009.0
+ Revision: 206986
- display correct default config file

* Wed May 14 2008 Funda Wang <fwang@mandriva.org> 0.2.2-4mdv2009.0
+ Revision: 206917
- drop libtoolize
- update abspath patch with ubuntu one

  + Götz Waschk <waschk@mandriva.org>
    - run libtoolize to fix build

* Tue May 13 2008 Funda Wang <fwang@mandriva.org> 0.2.2-3mdv2009.0
+ Revision: 206556
- drop static lib file
- disable arch specific optimizations
- add fedora patch to fix bug#40640:
    does not recognize absolute configure path

* Sun May 11 2008 Funda Wang <fwang@mandriva.org> 0.2.2-2mdv2009.0
+ Revision: 205607
- virtual provides for devel package

* Fri May 09 2008 Funda Wang <fwang@mandriva.org> 0.2.2-1mdv2009.0
+ Revision: 205311
- import source and spec
- Created package structure for wildmidi.

