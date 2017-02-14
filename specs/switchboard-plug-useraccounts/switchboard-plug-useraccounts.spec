%global debug_package %{nil}

Summary:        Switchboard User Accounts Plug
Name:           switchboard-plug-useraccounts
Version:        0.1.3+rev%{rev}
Release:        1%{?dist}
License:        LGPLv3
URL:            https://launchpad.net/switchboard-plug-useraccounts

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.34.1
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
Switchboard Plug for managing local user accounts.

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang useraccounts-plug


%files -f useraccounts-plug.lang
%doc AUTHORS
%license COPYING

%{_libdir}/switchboard/system/pantheon-useraccounts/

%{_datadir}/polkit-1/actions/org.pantheon.switchboard.user-accounts.policy


%changelog
* Tue Feb 14 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev280-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev279-1
- Update to latest snapshot.

* Fri Feb 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev278-1
- Update to latest snapshot.

* Thu Feb 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev277-1
- Update to latest snapshot.

* Wed Feb 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev276-1
- Update to latest snapshot.

* Mon Jan 30 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev275-1
- Update to latest snapshot.

* Sat Jan 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev274-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev273-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev272-1
- Update to latest snapshot.

* Tue Jan 24 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev271-1
- Update to latest snapshot.

* Mon Jan 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev270-1
- Update to latest snapshot.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev269-1
- Update to latest snapshot.

* Sun Jan 08 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev268-1
- Update to version 0.1.3.

* Fri Jan 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev267-1
- Update to version 0.1.3.

* Sun Dec 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev266-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev265-1
- Update to latest snapshot.

* Thu Dec 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev264-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev263-1
- Update to latest snapshot.

* Sun Dec 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev262-1
- Update to latest snapshot.

* Wed Nov 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3+rev261-1
- Update to version 0.1.3.


