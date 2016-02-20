%define rev 201

Summary: A simple screencasting app for the elementary project
Name: eidete
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv2
URL: http://launchpad.net/eidete

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(gdk-x11-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.10
BuildRequires: pkgconfig(libwnck-3.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xtst)

Requires: contractor


%description
Current features
- encoding to webm
- selection of the area to be recorded
- display of the pressed keys
- audio recording

Todo:
- create new contracts for facebook, youtube and others (waiting for gnome-online-accounts to be ready)
- improve and internationalize the key view


%prep
%autosetup


%build
export CFLAGS="-fPIC"
export CXXFLAGS="-fPIC"
export LDFLAGS="-fPIC"

%cmake
%make_build


%install
%make_install
%find_lang eidete

%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f eidete.lang
%doc README

%{_bindir}/eidete
%{_bindir}/videobin-uploader

%{_datadir}/applications/eidete.desktop
%{_datadir}/contractor/videobin.contract

%{_datadir}/icons/hicolor/48x48/apps/eidete.svg
%{_datadir}/icons/hicolor/48x48/apps/videobin.svg


%changelog
* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev201-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev200-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev199-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev198-1
- Update to new upstream snapshot.

* Sat Oct 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev197-1
- Update to new upstream snapshot.

* Fri Sep 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev196-1
- Try to fix f23-x64 build.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev196-2
- rebuild trigger for granite soname bump

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev196-1
- Initial package.



