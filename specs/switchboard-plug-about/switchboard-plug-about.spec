%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-about
Summary:        Switchboard System Information plug
Version:        0.2.4+git%{date}.%{commit}
Release:        1%{?dist}
License:        GPLv3+

URL:            https://github.com/elementary/switchboard-plug-about
Source0:        %{name}-%{version}.tar.gz

# Use official logo in the system details view
Patch0:         00-fedora-logo.patch

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard%{?_isa}

Requires:       system-logos


%description
This switchboard plug shows system information.


%prep
%autosetup -p1


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang about-plug


%files -f about-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/system/pantheon-about/


%changelog
* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.4+git170921.170550.974d3f19-1
- Initial package.


