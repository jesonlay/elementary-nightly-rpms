%define rev 268
%define debug_package %{nil}

Summary: Switchboard System Settings Power Plug
Name: switchboard-plug-power
Version: 0.2.2~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/switchboard-plug-power

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(gnome-settings-daemon)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Power Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-power-plug


%check
# Pantheon not recognised as DE in OnlyShowIn, so ignore for now
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-plug-power.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files -f pantheon-power-plug.lang
%{_libdir}/switchboard/hardware/pantheon-power/
# %{_datadir}/applications/pantheon-plug-power.desktop


%changelog
* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2~rev268-1
- Update to new upstream snapshot.

* Sun Nov 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2~rev267-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2~rev266-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.2~rev265-1
- omment=Update version tag to represent upstream version.

* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev265-1
- Update to new upstream snapshot.

* Tue Nov 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev264-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev263-1
- Update to new upstream snapshot.

* Fri Oct 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev262-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev261-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev260-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev259-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev258-1
- Update to new upstream snapshot.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev257-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev256-1
- Remove no longer shipped desktop file. Modernize spec.

* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev255-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev254-2
- rebuild trigger for granite soname bump

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev254-1
- Update to new upstream snapshot.

* Mon Aug 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev252-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev251-1
- Initial package.



