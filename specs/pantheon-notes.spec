Summary:        Simple note taking app for elementary OS
Name:           pantheon-notes
Version:        0.7~rev%{rev}
Release:        3%{?dist}
License:        GPLv3
URL:            http://launchpad.net/pantheon-notes

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  vala >= 0.26.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmime-2.6) >= 2.6.14
BuildRequires:  pkgconfig(granite) >= 0.3
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.10
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.10


%description
Simple note taking app for elementary OS


%prep
%autosetup


%build
CFLAGS="-fPIC $RPM_OPT_FLAGS"
LDFLAGS="-fPIC $RPM_OPT_FLAGS"

%cmake
%make_build


%install
%make_install
%find_lang pantheon-notes


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/pantheon-notes.desktop


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


%files -f pantheon-notes.lang
%{_bindir}/pantheon-notes

%{_datadir}/applications/pantheon-notes.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.notes.gschema.xml
%{_datadir}/pixmaps/pantheon-notes.svg


%changelog
* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev27-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev27-2
- Update for packaging changes.

* Fri May 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev27-1
- Update to latest snapshot.

* Mon May 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev26-1
- Update to latest snapshot.

* Fri May 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev25-1
- Update to latest snapshot.

* Thu May 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7~rev24-2
- Update for packaging changes.

* Thu May 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7-1
- Initial package.



