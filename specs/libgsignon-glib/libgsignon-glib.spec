# define used dbus type [p2p, session, system]
%global dbus_type session

Name:           libgsignon-glib
Summary:        GLib API for the SSO framework
Version:        2.4.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        LGPLv2

URL:            https://gitlab.com/accounts-sso/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)


Requires:       dbus%{?_isa}
Requires:       gsignond%{?_isa}


%description
This project is a library for managing single signon credentials which
can be used from GLib applications. It is effectively a GLib binding for
the D-Bus API provided by gsignond.


%package        devel
Summary:        GLib API for the SSO framework (development files)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This project is a library for managing single signon credentials which
can be used from GLib applications. It is effectively a GLib binding for
the D-Bus API provided by gsignond.

This package contains the development headers.


%package        example
Summary:        GLib API for the SSO framework (example client)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    example
This project is a library for managing single signon credentials which
can be used from GLib applications. It is effectively a GLib binding for
the D-Bus API provided by gsignond.

This package contains the example client.


%prep
%autosetup


%build
NOCONFIGURE=1 ./autogen.sh

%configure --enable-dbus-type=%{dbus_type}

%make_build


%install
%make_install

find %{buildroot} -name '*.la' -print -delete


%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%license COPYING

%{_libdir}/libgsignon-glib.so.1
%{_libdir}/libgsignon-glib.so.1.0.0

%{_libdir}/girepository-1.0/gSignon-1.0.typelib


%files          devel
%{_libdir}/libgsignon-glib.so
%{_libdir}/pkgconfig/libgsignon-glib.pc

%{_includedir}/libgsignon-glib/

%{_datadir}/gir-1.0/gSignon-1.0.gir
%{_datadir}/vala/vapi/libgsignon-glib.deps
%{_datadir}/vala/vapi/libgsignon-glib.vapi


%files          example
%{_bindir}/gsso-example


%changelog
* Sun May 06 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180504.164357.3058d420-1
- Update to latest snapshot.

* Sat Apr 14 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git180413.214955.0df5ad7f-1
- Update to latest snapshot.

* Wed Nov 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git171115.093207.5e9c8f71-1
- Update to latest snapshot.

* Sun Apr 23 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1+git161228.201347.03d9c64c-1
- Update to latest snapshot.

* Sat Apr 15 2017 Fabio Valentini <decathorpe@gmail.com> - 2.4.1-1.20161228.git03d9c64
- Initial package.

