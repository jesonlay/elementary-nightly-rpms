%define rev 63

Summary: Pantheon xsession settings
Name: pantheon-xsession-settings
Version: 0.5~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: https://code.launchpad.net/~elementary-os/elementaryos/pantheon-xsession-settings

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildArch: noarch

#BuildRequires: cmake
#BuildRequires: desktop-file-utils
#BuildRequires: gettext
#BuildRequires: vala

#BuildRequires: pkgconfig(granite)
#BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
#BuildRequires: pkgconfig(switchboard-2.0)


Requires: cerbere
Requires: gnome-session
Requires: gnome-settings-daemon


%description
Pantheon xsession settings


%prep
%setup -q


%build
rm autostart/cerbere.desktop


%install
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/xdg/autostart/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gconf/pantheon/default
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome-session/sessions
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pantheon
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xsessions

ln -s %{_datadir}/applications/cerbere.desktop $RPM_BUILD_ROOT/%{_sysconfdir}/xdg/autostart/cerbere.desktop

install autostart/* $RPM_BUILD_ROOT/%{_sysconfdir}/xdg/autostart/
install debian/pantheon.desktop $RPM_BUILD_ROOT/%{_datadir}/xsessions
install debian/pantheon.session $RPM_BUILD_ROOT/%{_datadir}/gnome-session/sessions
install gconf/pantheon/default/* $RPM_BUILD_ROOT/%{_datadir}/gconf/pantheon/default/
install gconf/pantheon.default.path $RPM_BUILD_ROOT/%{_datadir}/gconf/
install applications/* $RPM_BUILD_ROOT/%{_datadir}/pantheon/


%check


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files
%config %{_sysconfdir}/xdg/autostart/*
%{_datadir}/gconf/*
%{_datadir}/gnome-session/sessions/pantheon.session
%{_datadir}/pantheon
%{_datadir}/xsessions/pantheon.desktop


%changelog
* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.5~rev63-1
- Initial package.


