%define rev 115
%define debug_package %{nil}

Summary: A network indicator for wingpanel
Name: wingpanel-indicator-network
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-network

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-gtk)
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A network indicator for wingpanel.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang network-indicator


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f network-indicator.lang
%{_libdir}/wingpanel/libnetwork.so
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.network.gschema.xml


%changelog
* Tue Dec 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev115-1
- Update to new upstream snapshot.

* Mon Dec 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev114-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev113-1
- Update to new upstream snapshot.

* Wed Dec 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev112-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev111-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev110-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev109-1
- Update to new upstream snapshot.

* Sun Nov 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev108-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev107-1
- Update to new upstream snapshot.

* Wed Nov 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev106-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev105-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev104-1
- Update to new upstream snapshot.

* Thu Nov 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev103-1
- Update to new upstream snapshot.

* Wed Nov 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev102-1
- Update to new upstream snapshot.

* Tue Nov 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev103-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev102-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev100-1
- Update to new upstream snapshot.

* Thu Oct 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev97-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev96-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev91-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev90-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev89-1
- Update to new upstream snapshot.

* Sat Sep 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev88-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev87-1
- Update to new upstream snapshot.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev86-2
- Release bump for wingpanel soname change.

* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev86-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev85-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev84-1
- rebuild trigger for granite soname bump

* Sun Aug 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev83-1
- Update to new upstream snapshot.

* Sat Aug 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev82-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev81-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev80-1
- Update to new upstream snapshot.

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev75-1
- Update to new upstream snapshot.

* Sat Aug 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev56-1
- Update to bzr snapshot revno 56.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev42-1
- Initial package.


