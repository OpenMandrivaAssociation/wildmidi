%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		wildmidi
Version:	0.2.3.5
Release:	2
Summary:	WildMidi Open Source Midi Sequencer
Group:		Sound
License:	GPLv3+ and LGPLv3+
URL:		http://wildmidi.sourceforge.net
Source:		http://dfn.dl.sourceforge.net/sourceforge/wildmidi/%name-%version.tar.gz
Patch0:		wildmidi-0.2.3.4-fix-default-config-location.patch
BuildRequires:	timidity-instruments
BuildRequires:	pkgconfig(alsa)
Requires:	timidity-instruments

%description
WildMidi is a software midi play which has a core softsynth library that can be use with other applications.

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

