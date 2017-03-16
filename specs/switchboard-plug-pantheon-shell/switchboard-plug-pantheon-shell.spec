%global debug_package %{nil}

Summary:        Configure various aspects of the Pantheon desktop environment
Name:           switchboard-plug-pantheon-shell
Version:        0.2.4+rev%{rev}
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
The desktop plug is a section in Switchboard, the elementary System
Settings app, where users can configure the wallpaper, dock, and
hotcorners. In the future the desktop plug might also handle other
desktop settings such as the panel, app launcher, and window manager.

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
* Thu Mar 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev575-1
- Update to latest snapshot.

* Thu Mar 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev570-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev569-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev568-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev567-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev566-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev565-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev564-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev563-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev560-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev559-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev558-1
- Update to latest snapshot.

* Fri Feb 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev557-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev556-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev555-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev554-1
- Update to latest snapshot.

* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev553-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev552-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev551-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev546-1
- Update to latest snapshot.

* Wed Feb 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev545-1
- Update to latest snapshot.

* Tue Feb 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev544-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev543-1
- Update to latest snapshot.

* Fri Feb 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev542-1
- Update to latest snapshot.

* Fri Feb 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev541-1
- Update to latest snapshot.

* Tue Jan 31 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev540-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev539-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev538-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev537-1
- Update to latest snapshot.

* Thu Jan 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev536-1
- Update to latest snapshot.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev535-1
- Update to latest snapshot.

* Sun Jan 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev534-1
- Update to latest snapshot.

* Mon Jan 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev532-1
- Update to version 0.2.4.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev531-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev530-1
- Update to latest snapshot.

* Mon Dec 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev529-1
- Update to latest snapshot.

* Sun Dec 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev528-1
- Update to latest snapshot.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev527-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev526-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev525-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev523-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+rev522-1
- Update to version 0.2.4.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev522-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev521-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev520-1
- Update to latest snapshot.

* Fri Dec 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev519-1
- Update to latest snapshot.

* Wed Nov 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev518-1
- Update to latest snapshot.

* Sun Nov 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev517-1
- Update to latest snapshot.

* Sun Nov 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev516-1
- Update to latest snapshot.

* Sat Nov 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev513-1
- Update to latest snapshot.

* Fri Nov 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev512-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev511-1
- Update to latest snapshot.

* Wed Nov 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev510-1
- Update to latest snapshot.

* Fri Nov 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev509-1
- Update to latest snapshot.

* Thu Nov 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev508-1
- Update to latest snapshot.

* Tue Nov 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev507-1
- Update to latest snapshot.

* Mon Oct 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev506-1
- Update to latest snapshot.

* Sun Oct 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev505-1
- Update to latest snapshot.

* Fri Oct 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev504-1
- Update to latest snapshot.

* Thu Oct 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev503-1
- Update to latest snapshot.

* Thu Oct 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev502-1
- Update to latest snapshot.

* Mon Oct 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev499-1
- Update to latest snapshot.

* Sat Oct 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev498-1
- Update to latest snapshot.

* Thu Oct 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev497-1
- Update to latest snapshot.

* Fri Sep 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev496-1
- Update to latest snapshot.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev495-2
- Spec file cosmetics.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev495-1
- Update to latest snapshot.

* Fri Sep 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3+rev494-1
- Update to version 0.2.3.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev493-1
- Update to latest snapshot.

* Tue Sep 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev492-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev491-1
- Update to latest snapshot.

* Thu Sep 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev490-1
- Update to latest snapshot.

* Thu Sep 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev489-1
- Update to latest snapshot.

* Wed Sep 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev486-1
- Update to latest snapshot.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.3~rev485-1
- Update to version 0.2.3.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev480-1
- Update to latest snapshot.

* Thu Aug 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev479-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev477-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2.1~rev476-2
- Update for packaging changes.

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

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev449-1
- Initial package.


