%define rev 58
%define debug_package %{nil}

Summary: A session indicator for wingpanel
Name: wingpanel-indicator-session
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-session

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A session indicator for wingpanel.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang session-indicator


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig


%postun
/sbin/ldconfig


%files -f session-indicator.lang
%{_libdir}/wingpanel/libsession.so


%changelog
* Wed Dec 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev58-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev57-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev56-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev55-1
- Update to new upstream snapshot.

* Wed Nov 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev54-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev53-1
- Update to new upstream snapshot.

* Wed Nov 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev52-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev51-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev50-1
- Update to new upstream snapshot.

* Wed Oct 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev49-1
- Update to new upstream snapshot.

* Mon Oct 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev48-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev47-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev46-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev42-1
- Update to new upstream snapshot.

* Sun Oct 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev41-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev40-1
- Update to new upstream snapshot.

* Tue Oct 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev39-1
- Update to new upstream snapshot.

* Mon Oct 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev38-1
- Update to new upstream snapshot.

* Mon Oct 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev36-1
- Update to new upstream snapshot.

* Sun Sep 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev35-1
- Update to new upstream snapshot.

* Sat Sep 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev34-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev33-1
- Update to new upstream snapshot.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev31-2
- Release bump for wingpanel soname change.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev31-1
- rebuild trigger for granite soname bump

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev31-1
- Update to new upstream snapshot.

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev30-1
- Update to new upstream snapshot.

* Sat Aug 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev30-1
- Update to bzr snapshot revno 30.

* Thu Jul 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev28-1
- Update to bzr snapshot revno 28.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev23-1
- Initial package.


