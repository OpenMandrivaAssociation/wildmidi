%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Name: wildmidi
Version: 0.2.3.3
Release: %mkrel 1
Summary: WildMidi Open Source Midi Sequencer
Group: Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv3+ and LGPLv3+
URL: http://wildmidi.sourceforge.net
Source:	http://dfn.dl.sourceforge.net/sourceforge/wildmidi/%name-%version.tar.gz
#Patch0: wildmidi-0.2.2-opt.patch
#Patch1: wildmidi-0.2.2-cfg-abs-path.patch
#Patch2: wildmidi-0.2.2-pulseaudio.patch
Patch3: wildmidi-0.2.3.3-fix-default-config-location.patch
BuildRequires: timidity-instruments
BuildRequires: libalsa-devel
Requires: timidity-instruments

%description 
WildMidi is a software midi play which has a core softsynth library that can be use with other applications.

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.cfg.5*
%{_docdir}/%{name}/GPLv3.txt

#------------------------------------------------------------------------------------------------
%package -n %libname
Summary: Library for wildmidi
Group: System/Libraries

%description -n %libname
This package contains library files for wildmidi

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/*.so.%{major}*

#------------------------------------------------------------------------------------------------
%package -n %develname
Summary: Development files for wildmidi
Group: Development/Other
Requires: %libname = %version
Provides: %name-devel = %version

%description -n %develname
This package contains development files for wildmidi

%files -n %develname
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*.h
%{_mandir}/man3/*.3*
%{_docdir}/%{name}/LGPLv3.txt

#------------------------------------------------------------------------------------------------
%prep
%setup -q -n %name-%version
#%patch0 -p1 -b .opt
#%patch1 -p1 -b .abs
#%patch2 -p1 -b .pa
%patch3 -p0 -b .defconfig

%build
%configure2_5x --disable-static \
		--without-arch \
		--disable-werror
%make

%install
rm -rf %buildroot
%makeinstall_std

#install doc files
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
install -p docs/*v3.txt %{buildroot}%{_datadir}/doc/%{name}

%clean
rm -rf %buildroot
