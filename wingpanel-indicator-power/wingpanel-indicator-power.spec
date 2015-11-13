%define rev 100
%define debug_package %{nil}

Summary: A power indicator for wingpanel
Name: wingpanel-indicator-power
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel-indicator-power

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libbamf3)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(wingpanel-2.0)


%description
A power indicator for wingpanel.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang power-indicator

%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f power-indicator.lang
%{_libdir}/wingpanel/libpower.so
%{_datadir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.indicators.power.gschema.xml


%changelog
* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev100-1
- Update to new upstream snapshot.

* Wed Nov 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev99-1
- Update to new upstream snapshot.

* Mon Nov 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev97-1
- Update to new upstream snapshot.

* Mon Nov 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev96-1
- Update to new upstream snapshot.

* Sun Nov 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev95-1
- Update to new upstream snapshot.

* Fri Nov 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev94-1
- Update to new upstream snapshot.

* Thu Nov 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev93-1
- Update to new upstream snapshot.

* Wed Nov 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev92-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev91-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev90-1
- Update to new upstream snapshot.

* Mon Oct 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev88-1
- Update to new upstream snapshot.

* Sun Oct 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev86-1
- Update to new upstream snapshot.

* Sat Oct 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev85-1
- Update to new upstream snapshot.

* Fri Oct 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev84-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev83-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev82-1
- Update to new upstream snapshot.

* Sun Oct 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev81-1
- Update to new upstream snapshot.

* Fri Oct 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev80-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev79-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev78-1
- Update to new upstream snapshot.

* Sat Sep 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev77-1
- Update to new upstream snapshot.

* Wed Sep 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev76-1
- Update to new upstream snapshot.

* Tue Sep 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev75-1
- Update to new upstream snapshot.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev74-2
- Release bump for wingpanel soname change.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev74-1
- rebuild trigger for granite soname bump

* Mon Aug 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev74-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev73-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev72-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 0.1~rev71-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 0.1~rev70-2
- Add BRs libbamf3, libgtop-2.0.

* Mon Aug 17 2015 Fabio Valentini - 0.1~rev70-1
- Update to new upstream snapshot.

* Sat Aug 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev63-1
- Update to bzr snapshot revno 63.

* Tue Jul 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev57-1
- Initial package.


