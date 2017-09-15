%global debug_package %{nil}

Summary:        Configure all available networks
Name:           switchboard-plug-networking
Version:        0.1.0.3+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/switchboard-plug-networking

# The tarball is generated from a checkout of the specified branch and
# by executing 'bzr export' and has the usual format
# ('%{name}-%{version}.tar.gz'), where %{version} contains the upstream
# version number with a '+bzr%{rev}' suffix specifying the bzr revision.
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnm-glib)
BuildRequires:  pkgconfig(libnm-gtk)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard


%description
Configure all available networks

Designed for elementary OS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-network-plug


%files -f pantheon-network-plug.lang
%doc AUTHORS
%license COPYING

%{_libdir}/switchboard/network/pantheon-network/


%changelog
* Fri Sep 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev504-1
- Update to latest snapshot.

* Sat Aug 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev503-1
- Update to latest snapshot.

* Sat Jul 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev501-1
- Update to latest snapshot.

* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev495-1
- Update to latest snapshot.

* Wed Jun 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev491-1
- Update to latest snapshot.

* Sun Jun 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev490-1
- Update to latest snapshot.

* Tue May 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev384-1
- Update to latest snapshot.

* Sat May 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev383-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev382-1
- Update to latest snapshot.

* Wed Apr 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev381-1
- Update to latest snapshot.

* Wed Mar 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev380-1
- Update to latest snapshot.

* Sun Mar 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev379-1
- Update to latest snapshot.

* Tue Feb 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev378-1
- Update to latest snapshot.

* Thu Feb 23 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev377-1
- Update to latest snapshot.

* Sat Feb 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev376-1
- Update to latest snapshot.

* Mon Feb 13 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev375-1
- Update to latest snapshot.

* Sun Feb 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev374-1
- Update to latest snapshot.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev373-1
- Update to latest snapshot.

* Fri Jan 27 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev372-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev371-1
- Update to latest snapshot.

* Wed Jan 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev370-1
- Update to latest snapshot.

* Sat Jan 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev369-1
- Update to latest snapshot.

* Wed Jan 18 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev368-1
- Update to latest snapshot.

* Mon Jan 16 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev367-1
- Update to latest snapshot.

* Wed Jan 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev366-1
- Update to version 0.1.0.3.

* Tue Jan 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev365-1
- Update to version 0.1.0.3.

* Wed Jan 04 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev364-1
- Update to version 0.1.0.3.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev363-1
- Update to version 0.1.0.3.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev362-1
- Update to latest snapshot.

* Sun Jan 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev361-1
- Update to latest snapshot.

* Sat Dec 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev360-1
- Update to latest snapshot.

* Fri Dec 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev359-1
- Update to latest snapshot.

* Thu Dec 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev358-1
- Update to latest snapshot.

* Tue Dec 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev356-1
- Update to latest snapshot.

* Mon Dec 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev355-1
- Update to latest snapshot.

* Sat Dec 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev354-1
- Update to latest snapshot.

* Fri Dec 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev353-1
- Update to latest snapshot.

* Fri Dec 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev352-1
- Update to latest snapshot.

* Wed Dec 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev351-1
- Update to latest snapshot.

* Tue Dec 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev350-1
- Update to latest snapshot.

* Fri Dec 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev349-1
- Update to latest snapshot.

* Thu Dec 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev348-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev347-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev346-1
- Update to latest snapshot.

* Wed Dec 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev345-1
- Update to latest snapshot.

* Tue Dec 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev344-1
- Update to latest snapshot.

* Mon Dec 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev343-1
- Update to latest snapshot.

* Sun Dec 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev342-1
- Update to latest snapshot.

* Sat Dec 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev341-1
- Update to latest snapshot.

* Fri Dec 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.3+rev340-1
- Update to version 0.1.0.3.


