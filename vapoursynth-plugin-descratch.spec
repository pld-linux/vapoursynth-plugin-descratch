Summary:	DeScratch - Scratches Removing Filter
Summary(pl.UTF-8):	DeScratch - filtr usuwający zarysowania
Name:		vapoursynth-plugin-descratch
Version:	4
Release:	1
License:	GPL v2
Group:		Libraries
#Source0Download: https://github.com/vapoursynth/descratch/releases
Source0:	https://github.com/vapoursynth/descratch/archive/R%{version}/descratch-R%{version}.tar.gz
# Source0-md5:	5369093f30b27811860f7df30d50b742
Patch0:		descratch-system-libs.patch
URL:		https://github.com/vapoursynth/descratch
BuildRequires:	AviSynthPlus-devel
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	meson >= 1.2.3
BuildRequires:	ninja >= 1.5
BuildRequires:	python3 >= 1:3.12
BuildRequires:	vapoursynth-devel >= 77
Requires:	vapoursynth >= 77
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin removes vertical scratches from digitized films.

%description -l pl.UTF-8
Ta wtyczka usuwa pionowe zarysowania ze zdigitalizowanych filmów.

%prep
%setup -q -n descratch-R%{version}
%patch -P0 -p1

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md doc/{descratch.html,*.jpg}
%{py3_sitedir}/vapoursynth/plugins/descratch.so
