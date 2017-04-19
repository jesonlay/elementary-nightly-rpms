%global debug_package %{nil}

Summary:        Lightweight and stylish app launcher
Name:           slingshot-launcher
Version:        2.0.1+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/slingshot

# The tarball is generated from a checkout of the specified branch and
# by executing 'bzr export' and has the usual format
# ('%{name}-%{version}.tar.gz'), where %{version} contains the upstream
# version number with a '+bzr%{rev}' suffix specifying the bzr revision.
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.26.2
BuildRequires:  vala-tools

BuildRequires:  appstream-vala

BuildRequires:  pkgconfig(appstream) >= 0.10.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(plank) >= 0.10.9
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(unity) >= 4.0.0
BuildRequires:  pkgconfig(wingpanel-2.0)
BuildRequires:  pkgconfig(zeitgeist-2.0)


Requires:       zeitgeist


%description
The lightweight and stylish app launcher from elementary.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang slingshot


%files -f slingshot.lang
%doc AUTHORS
%license COPYING

%{_sysconfdir}/xdg/menus/pantheon-applications.menu

%{_libdir}/wingpanel/libslingshot.so

%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.slingshot.gschema.xml


%changelog
* Wed Apr 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev759-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev758-1
- Update to latest snapshot.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev757-2
- Add new BR: appstream.

* Sun Mar 26 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev757-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev756-1
- Update to latest snapshot.

* Wed Mar 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev755-1
- Update to latest snapshot.

* Tue Mar 14 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev754-1
- Update to latest snapshot.

* Wed Mar 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev753-1
- Update to latest snapshot.

* Thu Mar 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev752-1
- Update to latest snapshot.

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev751-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev750-1
- Update to latest snapshot.

* Mon Feb 27 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev749-1
- Update to latest snapshot.

* Sat Feb 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev748-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev747-1
- Update to latest snapshot.

* Mon Feb 20 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev746-1
- Update to latest snapshot.

* Sun Feb 19 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev745-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev743-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev742-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev741-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev740-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev739-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev738-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev737-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev736-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev735-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev734-1
- Update to latest snapshot.

* Mon Feb 06 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev733-1
- Update to latest snapshot.

* Sun Feb 05 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev732-1
- Update to latest snapshot.

* Sat Feb 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev731-1
- Update to latest snapshot.

* Thu Feb 02 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev730-1
- Update to latest snapshot.

* Tue Jan 31 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev729-1
- Update to latest snapshot.

* Tue Jan 31 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev728-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev726-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev725-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev724-1
- Update to latest snapshot.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev723-1
- Update to latest snapshot.

* Sun Jan 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev719-1
- Update to latest snapshot.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev718-1
- Update to version 2.0.1.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev717-1
- Update to version 2.0.1.

* Sat Jan 07 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev716-1
- Update to version 2.0.1.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev715-1
- Update to version 2.0.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0.1+rev714-1
- Update to version 2.0.1.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev714-1
- Update to version 2.0.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev711-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev710-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev708-2
- Enable libunity support.

* Sat Dec 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev708-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev707-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev706-1
- Update to latest snapshot.

* Tue Nov 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev705-1
- Update to latest snapshot.

* Mon Nov 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev704-1
- Update to latest snapshot.

* Wed Nov 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev703-1
- Update to latest snapshot.

* Tue Nov 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev702-1
- Update to latest snapshot.

* Mon Nov 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev701-1
- Update to latest snapshot.

* Mon Nov 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev700-1
- Update to latest snapshot.

* Thu Oct 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev699-1
- Update to latest snapshot.

* Sun Oct 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev698-1
- Update to latest snapshot.

* Fri Oct 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev697-1
- Update to latest snapshot.

* Thu Oct 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev696-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev695-1
- Update to latest snapshot.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev694-2
- Spec file cleanups.

* Mon Sep 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev694-1
- Update to latest snapshot.

* Sat Sep 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0+rev693-1
- Update to version 2.0.

* Wed Sep 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev692-1
- Update to latest snapshot.

* Fri Sep 16 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev691-1
- Update to latest snapshot.

* Thu Sep 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev690-1
- Update to latest snapshot.

* Wed Aug 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev689-1
- Update to latest snapshot.

* Fri Aug 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev688-1
- Update to latest snapshot.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~rev687-1
- Update to version 2.0.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev686-1
- Update to latest snapshot.

* Sun Aug 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev685-1
- Update to latest snapshot.

* Sat Aug 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev684-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev683-2
- Update for packaging changes.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev683-1
- Update to latest snapshot.

* Fri Aug 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev682-1
- Update to latest snapshot.

* Thu Aug 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev681-1
- Update to latest snapshot.

* Tue Aug 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev679-1
- Update to latest snapshot.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev678-1
- Update to latest snapshot.

* Sun Jul 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev677-1
- Update to latest snapshot.

* Sat Jul 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev676-1
- Update to latest snapshot.

* Thu Jul 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev675-1
- Update to latest snapshot.

* Mon Jul 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev674-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev673-1
- Update to latest snapshot.

* Mon Jul 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev672-1
- Update to latest snapshot.

* Fri Jul 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev671-1
- Update to latest snapshot.

* Thu Jul 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev670-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev669-2
- Update for packaging changes.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev669-1
- Update to latest snapshot.

* Tue Jul 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev668-1
- Update to latest snapshot.

* Mon Jul 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev667-1
- Update to latest snapshot.

* Sat Jul 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev666-1
- Update to latest snapshot.

* Fri Jul 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev665-1
- Update to latest snapshot.

* Wed Jun 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev664-1
- Update to latest snapshot.

* Tue Jun 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev663-1
- Update to latest snapshot.

* Thu Jun 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev662-1
- Update to latest snapshot.

* Tue Jun 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev661-1
- Update to latest snapshot.

* Sat Jun 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev660-1
- Update to latest snapshot.

* Wed Jun 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev659-1
- Update to latest snapshot.

* Tue Jun 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev658-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev657-4
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev657-3
- Update for packaging changes.

* Mon May 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev657-2
- Add missing "Requires: zeigeist" to fix crash at startup

* Sat May 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev657-1
- Update to latest snapshot.

* Sun May 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev656-1
- Update to latest snapshot.

* Thu May 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev655-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev654-1
- Update to latest snapshot.

* Tue May 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev653-1
- Update to latest snapshot.

* Sun May 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev652-1
- Update to latest snapshot.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.9.0~rev651-1
- Update for packaging changes.


