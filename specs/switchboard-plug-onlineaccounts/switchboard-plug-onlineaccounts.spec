%global __provides_exclude_from ^%{_libdir}/(pantheon-online-accounts)|(switchboard)/.*\\.so$

Name:           switchboard-plug-onlineaccounts
Summary:        Switchboard Online Accounts plug
Version:        0.3.0.1+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv2

URL:            https://github.com/elementary/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gsignond)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libgsignon-glib)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(switchboard-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Supplements:    switchboard%{?_isa}

Requires:       pantheon-online-accounts%{?_isa} = %{version}-%{release}


%description
%{summary}.


%package     -n pantheon-online-accounts
Summary:        Pantheon Online Accounts system (plugins)
Requires:       pantheon-online-accounts-libs%{?_isa} = %{version}-%{release}
%description -n pantheon-online-accounts
This package contains plugins for POA (Pantheon Online Accounts).


%package     -n pantheon-online-accounts-libs
Summary:        Pantheon Online Accounts system
%description -n pantheon-online-accounts-libs
This package contains the libraries making up POA (Pantheon Online
Accounts).


%package     -n pantheon-online-accounts-devel
Summary:        Pantheon Online Accounts system (development headers)
Requires:       pantheon-online-accounts-libs%{?_isa} = %{version}-%{release}
%description -n pantheon-online-accounts-devel
This package contains the development files for POA (Pantheon Online
Accounts).


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang pantheon-online-accounts


%post   -n pantheon-online-accounts-libs -p /sbin/ldconfig
%postun -n pantheon-online-accounts-libs -p /sbin/ldconfig


%files -f pantheon-online-accounts.lang
%{_libdir}/switchboard/network/pantheon-online-accounts/


%files       -n pantheon-online-accounts
%{_libdir}/pantheon-online-accounts/*

%{_datadir}/accounts/providers/*.provider
%{_datadir}/accounts/services/*.service
%{_datadir}/dbus-1/services/com.google.code.AccountsSSO.gSingleSignOnUI.service
%{_datadir}/icons/hicolor/*/apps/*.svg


%files       -n pantheon-online-accounts-libs
%license COPYING

%{_libdir}/libpantheon-online-accounts.so.0
%{_libdir}/libpantheon-online-accounts.so.0.1

%dir %{_libdir}/pantheon-online-accounts


%files       -n pantheon-online-accounts-devel
%{_includedir}/pantheon-online-accounts/

%{_libdir}/libpantheon-online-accounts.so
%{_libdir}/pkgconfig/pantheon-online-accounts.pc

%{_datadir}/vala/vapi/pantheon-online-accounts.deps
%{_datadir}/vala/vapi/pantheon-online-accounts.vapi


%changelog
* Sat Apr 29 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.0.1+git170417.235528.5a0270aa-1
- Initial package.


