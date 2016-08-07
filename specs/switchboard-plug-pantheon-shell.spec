%global debug_package %{nil}

Summary:        Configure various aspects of the Pantheon desktop environment
Name:           switchboard-plug-pantheon-shell
Version:        0.2.2.1~rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/switchboard-plug-pantheon-shell

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(plank)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       contractor


%description
The desktop plug is a section in Switchboard, the elementary System Settings app, where users can configure the wallpaper, dock, and hotcorners. In the future the desktop plug might also handle other desktop settings such as the panel, app launcher, and window manager.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-desktop-plug


%clean
rm -rf %{buildroot}


%files -f pantheon-desktop-plug.lang
%{_bindir}/set-wallpaper

%{_libdir}/switchboard/personal/pantheon-desktop/

%{_datadir}/contractor/set-wallpaper.contract


%changelog
* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev476-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev475-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev474-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev472-1
- Update to latest snapshot.

* Wed Jul 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev471-1
- Update to latest snapshot.

* Tue Jul 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev470-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev469-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev468-1
- Update to latest snapshot.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev467-1
- Update to latest snapshot.

* Fri Jul 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev466-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev465-2
- Update for packaging changes.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev457-1
- Update to latest snapshot.

* Fri Jun 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev456-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev455-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev454-1
- Update to latest snapshot.

* Sat Jun 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev453-1
- Update to latest snapshot.

* Thu Jun 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev452-1
- Update to latest snapshot.

* Sat Jun 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev451-1
- Update to latest snapshot.

* Fri Jun 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev450-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev449-4
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev449-3
- Update for packaging changes.

* Sat May 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev449-2
- Update for packaging changes.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev%{rev}-1
- Initial package.

