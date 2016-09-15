Summary:        fast and beautiful camera app
Name:           snap-photobooth
Version:        0.3~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/snap-elementary

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.24
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)


%description
A fast and beautiful camera app.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang snap-photobooth


%check
# desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f snap-photobooth.lang
%{_bindir}/snap-photobooth

%{_datadir}/appdata/snap-photobooth.appdata.xml
%{_datadir}/applications/snap-photobooth.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.snap.gschema.xml


%changelog
* Thu Sep 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev403-1
- Update to latest snapshot.

* Mon Sep 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev402-1
- Update to latest snapshot.

* Sun Sep 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev401-1
- Update to latest snapshot.

* Wed Aug 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev400-1
- Update to latest snapshot.

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev399-1
- Update to latest snapshot.

* Thu Aug 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev398-1
- Update to latest snapshot.

* Tue Aug 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev397-1
- Update to latest snapshot.

* Mon Aug 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev396-1
- Update to version 0.3.


