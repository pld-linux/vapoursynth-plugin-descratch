Summary:	DeScratch - Scratches Removing Filter
Summary(pl.UTF-8):	DeScratch - filtr usuwający zarysowania
Name:		vapoursynth-plugin-descratch
Version:	3
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://github.com/vapoursynth/descratch/archive/R%{version}/descratch-R%{version}.tar.gz
# Source0-md5:	f0a9f840689670169507a65b13fd0e1a
URL:		https://github.com/vapoursynth/descratch
BuildRequires:	AviSynthPlus-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	vapoursynth-devel >= 55
Requires:	vapoursynth >= 55
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin removes vertical scratches from digitized films.

%description -l pl.UTF-8
Ta wtyczka usuwa pionowe zarysowania ze zdigitalizowanych filmów.

%prep
%setup -q -n descratch-R%{version}

%build
libtool --tag=CXX --mode=compile %{__cxx} -c -o src/descratch.lo %{rpmcxxflags} %{rpmcppflags} $(pkg-config --cflags vapoursynth avisynth) src/descratch.cpp
libtool --tag=CXX --mode=link %{__cxx} -shared -module -avoid-version -o src/libdescratch.la %{rpmldflags} %{rpmcflags} src/descratch.lo -rpath %{_libdir}/vapoursynth

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/vapoursynth

libtool --mode=install install src/libdescratch.la $RPM_BUILD_ROOT%{_libdir}/vapoursynth

%{__rm} $RPM_BUILD_ROOT%{_libdir}/vapoursynth/libdescratch.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{descratch.html,*.jpg}
%attr(755,root,root) %{_libdir}/vapoursynth/libdescratch.so
