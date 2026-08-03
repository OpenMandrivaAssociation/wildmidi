%define	major 2
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname -d %{name}

Summary:	Open Source Midi Sequencer
Name:	wildmidi
Version:	0.5.0
Release:	1
License:	GPLv3+ and LGPLv3+
Group:	Sound
Url:	https://wildmidi.sourceforge.net
Source0:	https://github.com/Mindwerks/wildmidi/archive/%{name}-%{name}-%{version}.tar.gz
# dropped (no longer applies): Patch0:	wildmidi-0.5.0-bump-minimum-cmake-version.patch
BuildRequires:	make
BuildRequires:	cmake
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sndio)
# The player needs some soundfont
Requires:	timidity-instruments

%description
WildMidi is a software midi player which has a core softsynth library that can
be used with other applications.

%files
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.cfg.5*

#------------------------------------------------------------------------------------------------

%package -n %{libname}
Summary: Library for wildmidi
Group: System/Libraries

%description -n %{libname}
This package contains library files for wildmidi.

%files -n %{libname}
%{_libdir}/libWildMidi.so.%{major}*

#------------------------------------------------------------------------------------------------

%package -n %{develname}
Summary:	Development files for wildmidi
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains development files for wildmidi.

%files -n %{develname}
%{_libdir}/libWildMidi.so
%{_includedir}/wildmidi_lib.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/WildMidi/*.cmake
%{_mandir}/man3/*.3*

#------------------------------------------------------------------------------------------------

%prep
%autosetup p1 -n wildmidi-wildmidi-0.5.0


%build
%cmake -DWANT_ALSA=ON \
				-DWANT_SNDIO=ON \
				-DWANT_OPENAL=ON

%make_build


%install
%make_install -C build
