%define rev 176
%define debug_package %{nil}

Summary: Switchboard System Settings User Accounts Plug
Name: switchboard-plug-useraccounts
Version: 0.1.2~rev%{rev}
Release: 1%{?dist}
License: LGPLv3
URL: http://launchpad.net/switchboard-plug-useraccounts

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(pwquality)
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub User Accounts Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang useraccounts-plug


%check
# Pantheon not recognised as DE in OnlyShowIn, so ignore for now
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-plug-useraccounts.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files -f useraccounts-plug.lang
%{_libdir}/switchboard/system/pantheon-useraccounts
%{_datadir}/applications/pantheon-plug-useraccounts.desktop
%{_datadir}/polkit-1/actions/org.pantheon.switchboard.user-accounts.policy


%changelog
* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev176-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.2~rev175-1
- Initial package.



