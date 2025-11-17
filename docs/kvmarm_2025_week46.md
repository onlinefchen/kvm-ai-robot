# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-11-17 00:23:16

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 237
- **总 Thread 数**: 35
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 31 threads (194 邮件)
- **RFC**: 1 threads (36 邮件)
- **GIT PULL**: 1 threads (1 邮件)
- **Discussion**: 1 threads (4 邮件)
- **Other**: 1 threads (2 邮件)

---

## 📌 PATCH

共 31 个 thread

---

### Thread 1: [PATCH v2 00/45] KVM: arm64: Add LR overflow infrastructure

**📧 邮件数**: 35 | **👥 参与者**: 8 | **📅 开始时间**: Sun,  9 Nov 2025 17:15:34 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构上添加 LR（Link Register）溢出基础设施的补丁系列。

**原始补丁/问题的内容**：
Marc Zyngier 提出的补丁系列旨在解决 VGIC（虚拟通用中断控制器）中的一些严重错误，并引入了 LR 溢出处理机制。这一补丁经过多次迭代，包含了错误修复、优化以及测试用例。

**之前的讨论要点**：
在历史讨论中，Marc 详细介绍了补丁的背景，强调了对多种 ARM 设备的广泛测试，特别是一些存在已知缺陷的设备（如 Apple 和 Qualcomm）。补丁的目标是改善对中断的处理，尤其是在 LR 容量溢出时的行为。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现和测试结果上。Yao Yuan 和 Marc 就补丁的逻辑进行了深入讨论，确认了对 vLPI 和 vSPI 的处理方式。Suzuki 提出了需要在某些情况下添加保护措施的建议。Marek Szyprowski 报告了在 Raspberry Pi 5 和 Amlogic SM1 板上出现的启动故障，Marc 随后提出了可能的解决方案。Fuad Tabba 进一步分析了在 QEMU 环境下的测试结果，并提出了一些修复建议。最终，Marc 表示将继续研究并计划在下周进行清理工作。整体来看，补丁的实施进展顺利，但仍需解决一些特定硬件上的问题。

#### 📝 邮件列表

1. **[11-09 17:15]** [PATCH v2 00/45] KVM: arm64: Add LR overflow infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-09 17:15]** [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a patched-in constant
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-09 17:15]** [PATCH v2 05/45] KVM: arm64: GICv3: Detect and work around the lack of ICV_DIR_EL1 trapping
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[11-09 17:15]** [PATCH v2 12/45] KVM: arm64: GICv3: Extract LR folding primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[11-09 17:15]** [PATCH v2 20/45] KVM: arm64: Revamp vgic maintenance interrupt configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[11-09 17:16]** [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when interrupts overflow LR capacity
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[11-10 17:01]** Re: [PATCH v2 12/45] KVM: arm64: GICv3: Extract LR folding primitive
   - 发件人: Yao Yuan <yaoyuan@linux.alibaba.com>
8. **[11-10 09:18]** Re: [PATCH v2 12/45] KVM: arm64: GICv3: Extract LR folding primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[11-10 17:48]** Re: [PATCH v2 12/45] KVM: arm64: GICv3: Extract LR folding primitive
   - 发件人: Yao Yuan <yaoyuan@linux.alibaba.com>
10. **[11-10 10:40]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a
 patched-in constant
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
11. **[11-10 11:47]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a patched-in constant
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[11-11 15:53]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a
 patched-in constant
   - 发件人: Oliver Upton <oupton@kernel.org>
13. **[11-11 16:08]** Re: [PATCH v2 20/45] KVM: arm64: Revamp vgic maintenance interrupt
 configuration
   - 发件人: Oliver Upton <oupton@kernel.org>
14. **[11-12 08:33]** Re: [PATCH v2 20/45] KVM: arm64: Revamp vgic maintenance interrupt configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[11-12 00:45]** Re: [PATCH v2 20/45] KVM: arm64: Revamp vgic maintenance interrupt
 configuration
   - 发件人: Oliver Upton <oupton@kernel.org>
16. **[11-12 01:13]** Re: [PATCH v2 00/45] KVM: arm64: Add LR overflow infrastructure
   - 发件人: Oliver Upton <oupton@kernel.org>
17. **[11-12 09:56]** Re: [PATCH v2 20/45] KVM: arm64: Revamp vgic maintenance interrupt configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[11-13 10:52]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a
 patched-in constant
   - 发件人: Marek Szyprowski <m.szyprowski@samsung.com>
19. **[11-13 10:56]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a patched-in constant
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[11-13 10:59]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a patched-in constant
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[11-13 12:04]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a
 patched-in constant
   - 发件人: Marek Szyprowski <m.szyprowski@samsung.com>
22. **[11-13 12:20]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a
 patched-in constant
   - 发件人: Marek Szyprowski <m.szyprowski@samsung.com>
23. **[11-13 11:23]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a
 patched-in constant
   - 发件人: Joey Gouly <joey.gouly@arm.com>
24. **[11-13 11:42]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a patched-in constant
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[11-13 14:33]** Re: [PATCH v2 05/45] KVM: arm64: GICv3: Detect and work around the
 lack of ICV_DIR_EL1 trapping
   - 发件人: Mark Brown <broonie@kernel.org>
26. **[11-13 18:01]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a
 patched-in constant
   - 发件人: Mark Brown <broonie@kernel.org>
27. **[11-13 18:15]** Re: [PATCH v2 05/45] KVM: arm64: GICv3: Detect and work around the lack of ICV_DIR_EL1 trapping
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[11-13 19:06]** Re: [PATCH v2 05/45] KVM: arm64: GICv3: Detect and work around the
 lack of ICV_DIR_EL1 trapping
   - 发件人: Mark Brown <broonie@kernel.org>
29. **[11-13 20:10]** Re: [PATCH v2 05/45] KVM: arm64: GICv3: Detect and work around the lack of ICV_DIR_EL1 trapping
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[11-13 13:59]** Re: [PATCH v2 05/45] KVM: arm64: GICv3: Detect and work around the
 lack of ICV_DIR_EL1 trapping
   - 发件人: Oliver Upton <oupton@kernel.org>
31. **[11-14 09:37]** Re: [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a patched-in constant
   - 发件人: Marc Zyngier <maz@kernel.org>
32. **[11-14 14:20]** Re: [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when
 interrupts overflow LR capacity
   - 发件人: Fuad Tabba <tabba@google.com>
33. **[11-14 15:02]** Re: [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when interrupts overflow LR capacity
   - 发件人: Marc Zyngier <maz@kernel.org>
34. **[11-14 15:53]** Re: [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when
 interrupts overflow LR capacity
   - 发件人: Fuad Tabba <tabba@google.com>
35. **[11-14 17:41]** Re: [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when interrupts overflow LR capacity
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH v7 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 15 | **👥 参与者**: 5 | **📅 开始时间**: Fri, 7 Nov 2025 15:21:20 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 Linux 内核中添加对 Armv8.7 特性 FEAT_{LS64, LS64_V} 的支持及相关测试的补丁（PATCH v7 0/7）。该补丁旨在实现单拷贝原子64字节加载和存储指令的支持，具体内容包括在 cpufeature 列表中添加识别和启用这些特性、通过 HWCAP3 和 cpuinfo 向用户空间暴露这些特性、添加相关的硬件能力测试，以及在虚拟机中处理不支持的内存访问的陷阱。

在历史讨论中，参与者们主要集中在补丁的实现细节上，包括如何在用户空间和虚拟机中正确处理这些新特性，以及补丁的顺序和文档更新等问题。特别是，Suzuki K Poulose 提出了关于 EXIT 原因的文档化和补丁顺序的建议，Oliver Upton 指出某些补丁的顺序不当。

在本周的新讨论中，Zhou Wang 和其他参与者继续讨论补丁的细节，特别是关于如何安全地将这些特性暴露给用户空间的问题。Marc Zyngier 表达了对直接暴露这些特性的担忧，认为需要系统提供强有力的保证。Arnd Bergmann 则讨论了与特定设备的兼容性问题，并询问了设备如何处理 PASID 数据。Zhou Wang 最终确认了他们的 SoC 中有实际设备支持这些特性，并表示设备的处理方式与 PASID 数据无关。

整体来看，本周的讨论进一步深化了对补丁实现的理解，并探讨了安全性和兼容性方面的挑战。

#### 📝 邮件列表

1. **[11-07 15:21]** [PATCH v7 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[11-07 15:21]** [PATCH v7 1/7] KVM: arm64: Add exit to userspace on {LD,ST}64B* outside of memslots
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
3. **[11-07 15:21]** [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
4. **[11-07 15:21]** [PATCH v7 6/7] KVM: arm64: Enable FEAT_{LS64, LS64_V} in the supported guest
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
5. **[11-07 11:48]** Re: [PATCH v7 1/7] KVM: arm64: Add exit to userspace on {LD,ST}64B*
 outside of memslots
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
6. **[11-07 12:05]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
7. **[11-07 10:53]** Re: [PATCH v7 6/7] KVM: arm64: Enable FEAT_{LS64, LS64_V} in the
 supported guest
   - 发件人: Oliver Upton <oupton@kernel.org>
8. **[11-11 10:12]** Re: [PATCH v7 1/7] KVM: arm64: Add exit to userspace on {LD,ST}64B*
 outside of memslots
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
9. **[11-11 11:40]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
10. **[11-11 11:43]** Re: [PATCH v7 6/7] KVM: arm64: Enable FEAT_{LS64, LS64_V} in the
 supported guest
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
11. **[11-11 11:15]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[11-13 22:40]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
13. **[11-13 17:26]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Arnd Bergmann <arnd@arndb.de>
14. **[11-14 17:25]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
15. **[11-14 10:37]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Arnd Bergmann <arnd@arndb.de>

---

### Thread 3: [PATCH v2 0/2] use TPM device with CRB over FF-A when kernel boot with pkvm

**📧 邮件数**: 14 | **👥 参与者**: 6 | **📅 开始时间**: Thu, 30 Oct 2025 10:22:43 +0000

#### 🤖 AI 总结

本邮件线程讨论了在使用 pkvm 启动内核时，通过 FF-A 使用 CRB 的 TPM 设备的相关补丁和问题。

**原始补丁/问题内容**：
Yeoreum Yun 提出的补丁系列旨在解决在使用 `kvm-arm.mode=protected` 启动时，内核无法探测 TPM 设备的问题。该问题源于 FF-A 调用失败，导致无法生成包含 PCR 值的 boot_aggregate 日志。

**之前讨论要点**：
历史讨论中，补丁的第一部分修复了当 FF-A 驱动作为内置模块时 FF-A 调用失败的问题。Per Larsen 和其他参与者讨论了 FF-A 直接消息的支持，强调了该补丁的必要性和用例。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的审查和改进上。Eric Auger 对补丁提出了建议，要求在未覆盖 PSCI 版本时返回默认值。Will Deacon 则质疑 FF-A 初始化的时机，认为在 pKVM 初始化之前使用 FF-A 可能会导致更大的问题。Yeoreum Yun 进一步解释了 IMA 模块构建的限制，并指出当前问题的根源在于 FF-A 驱动的初始化顺序。整体来看，讨论仍在进行中，参与者们在寻求最佳解决方案。

#### 📝 邮件列表

1. **[10-30 10:22]** [PATCH v2 0/2] use TPM device with CRB over FF-A when kernel boot with pkvm
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[10-30 10:22]** [PATCH v2 1/2] KVM: arm64: fix FF-A call failure when ff-a driver is built-in
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[10-30 15:49]** [PATCH v2 0/2] KVM: arm64: Support FF-A direct messaging
 interfaces
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[10-30 15:49]** [PATCH v2 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in host
 handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[10-30 17:59]** [PATCH v2 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
6. **[10-30 17:59]** [PATCH v2 1/2] target/arm/kvm: add constants for new PSCI versions
   - 发件人: Sebastian Ott <sebott@redhat.com>
7. **[10-30 17:59]** [PATCH v2 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
8. **[11-11 18:50]** Re: [PATCH v2 1/2] target/arm/kvm: add constants for new PSCI
 versions
   - 发件人: Eric Auger <eric.auger@redhat.com>
9. **[11-11 18:57]** Re: [PATCH v2 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Eric Auger <eric.auger@redhat.com>
10. **[11-11 20:16]** Re: [PATCH v2 0/2] arm64: Replace __ASSEMBLY__ with __ASSEMBLER__ in headers
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
11. **[11-12 18:20]** Re: [PATCH v2 2/2] target/arm/kvm: add kvm-psci-version vcpu
 property
   - 发件人: Sebastian Ott <sebott@redhat.com>
12. **[11-14 16:24]** Re: [PATCH v2 1/2] KVM: arm64: fix FF-A call failure when ff-a
 driver is built-in
   - 发件人: Will Deacon <will@kernel.org>
13. **[11-14 17:41]** Re: [PATCH v2 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in
 host handler
   - 发件人: Will Deacon <will@kernel.org>
14. **[11-14 20:14]** Re: [PATCH v2 1/2] KVM: arm64: fix FF-A call failure when ff-a
 driver is built-in
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 4: [PATCH 00/12] KVM: arm64: nv: Implement FEAT_XNX and FEAT_HAF

**📧 邮件数**: 13 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 12 Nov 2025 10:33:54 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下实现 FEAT_XNX 和 FEAT_HAF 的补丁系列（PATCH 00/12）。这些补丁旨在填补 KVM 的影子阶段 2 实现与架构之间的差距。

**原始补丁内容**：
补丁系列主要包括对 FEAT_XNX 和 FEAT_HAF 的支持。FEAT_XNX 允许在阶段 2 中为 EL0 和 EL1 编码不同的执行权限，而 FEAT_HAF 则涉及在用户内存中原子更新描述符以设置访问标志。

**之前讨论要点**：
在历史讨论中，虽然没有具体的邮件记录，但可以推测，之前的讨论可能集中在如何实现这些功能的架构设计和实现细节上。

**本周新讨论与进展**：
本周的讨论中，Oliver Upton 提出了多个补丁，逐步实现了对 FEAT_XNX 和 FEAT_HAF 的支持，包括：
1. 检测 FEAT_XNX 特性。
2. 为阶段 2 权限添加 FEAT_XNX 支持。
3. 将 FEAT_XNX 权限转发到影子阶段 2。
4. 更新 ptdump 以显示 FEAT_XNX 权限。
5. 实现对硬件访问标志的管理，并将其暴露给 NV 客户端。

整体来看，这些补丁的实现仍在进行中，且由于缺乏 NV 能力的测试设备，部分功能尚未经过充分测试。开发者计划在未来增加自测覆盖率。

#### 📝 邮件列表

1. **[11-12 10:33]** [PATCH 00/12] KVM: arm64: nv: Implement FEAT_XNX and FEAT_HAF
   - 发件人: Oliver Upton <oupton@kernel.org>
2. **[11-12 10:33]** [PATCH 01/12] arm64: Detect FEAT_XNX
   - 发件人: Oliver Upton <oupton@kernel.org>
3. **[11-12 10:33]** [PATCH 02/12] KVM: arm64: Add support for FEAT_XNX stage-2 permissions
   - 发件人: Oliver Upton <oupton@kernel.org>
4. **[11-12 10:33]** [PATCH 03/12] KVM: arm64: nv: Forward FEAT_XNX permissions to the shadow stage-2
   - 发件人: Oliver Upton <oupton@kernel.org>
5. **[11-12 10:33]** [PATCH 04/12] KVM: arm64: Teach ptdump about FEAT_XNX permissions
   - 发件人: Oliver Upton <oupton@kernel.org>
6. **[11-12 10:33]** [PATCH 05/12] KVM: arm64: nv: Advertise support for FEAT_XNX
   - 发件人: Oliver Upton <oupton@kernel.org>
7. **[11-12 10:34]** [PATCH 06/12] KVM: arm64: Call helper for reading descriptors directly
   - 发件人: Oliver Upton <oupton@kernel.org>
8. **[11-12 10:34]** [PATCH 07/12] KVM: arm64: Handle endianness in read helper for emulated PTW
   - 发件人: Oliver Upton <oupton@kernel.org>
9. **[11-12 10:34]** [PATCH 08/12] KVM: arm64: nv: Use pgtable definitions in stage-2 walk
   - 发件人: Oliver Upton <oupton@kernel.org>
10. **[11-12 10:34]** [PATCH 09/12] KVM: arm64: Add helper for swapping guest descriptor
   - 发件人: Oliver Upton <oupton@kernel.org>
11. **[11-12 10:34]** [PATCH 10/12] KVM: arm64: Implement HW access flag management in stage-1 SW PTW
   - 发件人: Oliver Upton <oupton@kernel.org>
12. **[11-12 10:34]** [PATCH 11/12] KVM: arm64: nv: Implement HW access flag management in stage-2 SW PTW
   - 发件人: Oliver Upton <oupton@kernel.org>
13. **[11-12 10:34]** [PATCH 12/12] KVM: arm64: nv: Expose hardware access flag management to NV guests
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 5: [PATCH v4 0/8] KVM: arm64: Fixes for guest CPU feature trapping and enabling

**📧 邮件数**: 12 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 12 Nov 2025 09:20:43 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的多个修复补丁，主要集中在来宾 CPU 特性捕获和启用方面。

**原始补丁内容**：
本次补丁系列（PATCH v4 0/8）包含了针对来宾特性捕获和启用的多项修复，以及一些代码整理。补丁主要解决了 MTE（内存标记扩展）标志传播的问题，并对 pKVM（保护虚拟机）下的特性检查进行了增强。

**之前讨论要点**：
在之前的讨论中，开发者们关注了如何确保在保护模式下正确处理特性和 IOCTL（输入输出控制）请求，特别是 MTE 特性的复杂性和对虚拟机的影响。

**本周新讨论和进展**：
本周的讨论中，Fuad Tabba 提出了多个补丁，主要包括：
1. 修复了保护虚拟机中 Trace Buffer 的捕获逻辑。
2. 修复了 MTE 标志初始化的逻辑，确保仅在允许的情况下设置该标志。
3. 引入了用于计算故障 IPA 偏移的辅助函数，提升代码可读性。
4. 扩展了 pKVM 的能力检查，确保在保护模式下不允许 MTE 特性。
5. 引入了对 VM IOCTL 是否被允许的检查，确保只有支持的特性才能执行相应的 IOCTL。

此外，参与者对补丁进行了审查，Ben Horgan 和 Oliver Upton 表达了支持并提出了进一步的建议。整体上，本周的讨论推动了补丁的完善和功能的增强。

#### 📝 邮件列表

1. **[11-12 09:20]** [PATCH v4 0/8] KVM: arm64: Fixes for guest CPU feature trapping and enabling
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[11-12 09:20]** [PATCH v4 1/8] KVM: arm64: Fix Trace Buffer trapping for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[11-12 09:20]** [PATCH v4 2/8] KVM: arm64: Fix Trace Buffer trap polarity for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[11-12 09:20]** [PATCH v4 3/8] KVM: arm64: Fix MTE flag initialization for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[11-12 09:20]** [PATCH v4 4/8] KVM: arm64: Introduce helper to calculate fault IPA offset
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[11-12 09:20]** [PATCH v4 5/8] KVM: arm64: Include VM type when checking VM
 capabilities in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[11-12 09:20]** [PATCH v4 6/8] KVM: arm64: Do not allow KVM_CAP_ARM_MTE for any guest
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[11-12 09:20]** [PATCH v4 7/8] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[11-12 09:20]** [PATCH v4 8/8] KVM: arm64: Prevent host from managing timer offsets
 for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[11-12 09:39]** Re: [PATCH v4 3/8] KVM: arm64: Fix MTE flag initialization for
 protected VMs
   - 发件人: Ben Horgan <ben.horgan@arm.com>
11. **[11-12 02:07]** Re: [PATCH v4 7/8] KVM: arm64: Check whether a VM IOCTL is allowed
 in pKVM
   - 发件人: Oliver Upton <oupton@kernel.org>
12. **[11-12 10:51]** Re: [PATCH v4 7/8] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 6: [PATCH v4 1/3] KVM: arm64: VM exit to userspace to handle SEA

**📧 邮件数**: 11 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 3 Nov 2025 18:17:00 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下处理 SEAs（Synchronous External Abort）的补丁（PATCH v4 1/3）。该补丁旨在实现虚拟机退出到用户空间以处理 SEA。

在历史讨论中，参与者对补丁的有效性进行了质疑，特别是关于数据中止（Data Abort）检查的有效性，以及 PFAR_EL2 寄存器的使用。Jose Marinho 和 Jiaqi Yan 讨论了补丁的细节，确认 VNCR 位确实与数据中止相关，而不需要排除指令中止的检查。

在本周的新讨论中，Jiaqi Yan 对先前的反馈表示感谢，并询问是否还有其他对 API 和实现的顾虑。Oliver Upton 提出，补丁需要检查数据中止的情况。Mauro Carvalho Chehab 则建议使用更通用的名称替换 KVM_EXIT_ARM_SEA，以便更好地反映其功能，并强调需要在实际用户空间应用程序中进行测试。Oliver Upton 也对补丁进行了清理，并确认所有问题已得到解决，补丁将被应用到下一个版本中。

总的来说，本周的讨论集中在补丁的命名、实现细节和测试需求上，参与者们对补丁的进一步完善达成了一致。

#### 📝 邮件列表

1. **[11-03 18:17]** Re: [PATCH v4 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jose Marinho <jose.marinho@arm.com>
2. **[11-03 12:45]** Re: [PATCH v4 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[11-10 09:41]** Re: [PATCH v4 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
4. **[11-11 01:53]** Re: [PATCH v4 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Oliver Upton <oupton@kernel.org>
5. **[11-11 15:32]** Re: [PATCH v4 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
6. **[11-13 14:54]** Re: [PATCH v4 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Mauro Carvalho Chehab <mchehab+huawei@kernel.org>
7. **[11-13 10:21]** Re: [PATCH v4 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[11-13 13:06]** Re: [PATCH v4 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Oliver Upton <oupton@kernel.org>
9. **[11-13 14:14]** Re: [PATCH v4 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
10. **[11-13 14:33]** Re: [PATCH v4 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Oliver Upton <oupton@kernel.org>
11. **[11-13 16:53]** Re: [PATCH v4 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 7: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct map

**📧 邮件数**: 11 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 31 Oct 2025 17:30:12 +0000

#### 🤖 AI 总结

本邮件线程讨论的是一个关于 KVM（内核虚拟机）的补丁，主题为“添加标志以从直接映射中移除 guest_memfd”。该补丁的目的是为不支持直接映射的架构提供一个标志，以便在这些架构上能够正确处理 guest_memfd。

在历史讨论中，参与者们主要关注了补丁的实现细节，特别是如何处理不同架构对 `set_direct_map` 功能的支持。Brendan Jackman 和 Mike Rapoport 讨论了在不支持 `ARCH_HAS_SET_DIRECT_MAP` 的架构上，如何定义 `can_set_direct_map()` 函数以避免潜在的错误。讨论中提到了一些存根函数的存在，这些函数在不支持直接映射的架构上返回 0，但也引发了对如何处理这些架构的进一步思考。

在本周的新讨论中，Mike Rapoport 确认了之前的观点，即对于不支持 `set_direct_map` 的架构，确实应该将 `can_set_direct_map` 定义为 false。此外，Brendan Jackman 表示，Nikita Kalyazin 已经成功构建了一个分支，并确认了崩溃问题已经解决，但这可能会阻碍该功能的合并。因此，参与者们需要进一步确认哪些补丁可能与崩溃问题相关，以便进行修复和合并。

#### 📝 邮件列表

1. **[10-31 17:30]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Brendan Jackman <jackmanb@google.com>
2. **[11-01 11:39]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>
3. **[11-03 10:35]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Brendan Jackman <jackmanb@google.com>
4. **[11-03 12:50]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>
5. **[11-04 11:08]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Brendan Jackman <jackmanb@google.com>
6. **[11-07 15:54]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Brendan Jackman <jackmanb@google.com>
7. **[11-07 17:23]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
8. **[11-07 18:04]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Brendan Jackman <jackmanb@google.com>
9. **[11-07 18:11]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
10. **[11-10 14:34]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>
11. **[11-10 15:36]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Brendan Jackman <jackmanb@google.com>

---

### Thread 8: [PATCH v3 0/8] KVM: arm64: Fixes for guest CPU feature trapping and enabling

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 10 Nov 2025 13:45:17 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的修复补丁，主要集中在来宾 CPU 特性捕获和启用方面。

1. **原始补丁内容**：该补丁系列（PATCH v3 0/8）包含多个修复，旨在解决来宾特性捕获和启用的问题，并进行代码整理。补丁包括引入新的辅助函数、扩展能力检查、限制某些虚拟机类型的功能等。

2. **之前讨论要点**：在历史讨论中，参与者曾对补丁的内容进行了初步评审，强调了对特定功能的支持限制，尤其是在受保护虚拟机（pKVM）中，某些功能如 MTE（内存标签扩展）不应被允许。

3. **本周的新讨论与进展**：本周的讨论中，Fuad Tabba 提出了具体的补丁实现，逐一修复了与 Trace Buffer、MTE 标志初始化、IOCTL 检查等相关的问题。Ben Horgan 对 MTE 标志初始化的逻辑提出了质疑，Fuad 随后确认了修复方向并表示感谢。此外，补丁还明确禁止在 pKVM 中对所有虚拟机类型启用 MTE，并引入了新的检查机制以确保 IOCTL 的合规性。

总体而言，本周的讨论推动了补丁的完善，并解决了多个关键问题，确保了 KVM 在 arm64 架构下的稳定性和安全性。

#### 📝 邮件列表

1. **[11-10 13:45]** [PATCH v3 0/8] KVM: arm64: Fixes for guest CPU feature trapping and enabling
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[11-10 13:45]** [PATCH v3 1/8] KVM: arm64: Fix Trace Buffer trapping for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[11-10 13:45]** [PATCH v3 2/8] KVM: arm64: Fix Trace Buffer trap polarity for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[11-10 13:45]** [PATCH v3 3/8] KVM: arm64: Fix MTE flag initialization for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[11-10 13:45]** [PATCH v3 4/8] KVM: arm64: Introduce helper to calculate fault IPA offset
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[11-10 13:45]** [PATCH v3 5/8] KVM: arm64: Include VM type when checking VM
 capabilities in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[11-10 13:45]** [PATCH v3 6/8] KVM: arm64: Do not allow KVM_CAP_ARM_MTE for any guest
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[11-10 13:45]** [PATCH v3 7/8] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[11-10 13:45]** [PATCH v3 8/8] KVM: arm64: Prevent host from managing timer offsets
 for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[11-10 14:51]** Re: [PATCH v3 3/8] KVM: arm64: Fix MTE flag initialization for
 protected VMs
   - 发件人: Ben Horgan <ben.horgan@arm.com>
11. **[11-10 15:03]** Re: [PATCH v3 3/8] KVM: arm64: Fix MTE flag initialization for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 9: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations

**📧 邮件数**: 10 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 28 Oct 2025 11:44:06 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 自测试的一个补丁，主题为“修复未对齐的 mmap 分配”。该补丁旨在解决由于不对齐的 `map_size` 导致的 `munmap()` 失败问题，特别是在进行预取测试时。

在历史讨论中，参与者指出，由于在测试中引入了一个选项来改变后备页大小，导致了一些测试失败。Jack Thomson 和 Sean Christopherson 讨论了是否应该在 `vm_mem_add()` 中处理这些测试问题，最终达成共识，认为测试应自行处理大小和对齐问题，以避免掩盖潜在的测试缺陷。

本周的新讨论中，Jack Thomson 表示将更新补丁以解决之前提到的问题。Mark Brown 提出了与 ARM64 相关的其他补丁，旨在改善测试的诊断信息，包括逐个报告寄存器的测试结果，以便更清晰地识别问题。此外，Brown 还提出了对某些测试的非致命断言进行修改，以提高可用性和测试的准确性。

总体而言，讨论集中在如何改进 KVM 自测试的稳定性和可读性，确保测试结果能够准确反映系统状态。

#### 📝 邮件列表

1. **[10-28 11:44]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Thomson, Jack <jackabt.amazon@gmail.com>
2. **[11-03 13:08]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[11-04 11:40]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Thomson, Jack <jackabt.amazon@gmail.com>
4. **[11-04 12:19]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[11-13 11:34]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Thomson, Jack <jackabt.amazon@gmail.com>
6. **[11-14 15:35]** [PATCH v2 0/4] KVM: selftests: arm64: Improve diagnostics from
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[11-14 15:35]** [PATCH v2 1/4] KVM: selftests: arm64: Report set_id_reg reads of
 test registers as tests
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[11-14 15:35]** [PATCH v2 2/4] KVM: selftests: arm64: Report register reset tests
 individually
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[11-14 15:35]** [PATCH v2 3/4] KVM: selftests: arm64: Make set_id_regs bitfield
 validatity checks non-fatal
   - 发件人: Mark Brown <broonie@kernel.org>
10. **[11-14 15:35]** [PATCH v2 4/4] KVM: selftests: arm64: Skip all 32 bit IDs when
 set_id_regs is aarch64 only
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 10: [PATCH v9 0/5] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 29 Oct 2025 15:46:00 +0000

#### 🤖 AI 总结

本邮件线程讨论的是针对 ARMv8.8 SPE 特性的补丁，主要集中在数据源过滤功能的实现上。

1. **原始补丁内容**：James Clark 提出了一个包含五个补丁的系列，主要目的是支持 SPE_FEAT_FDS 数据源过滤。补丁中包括新增 `perf_event_attr::config4` 字段，以便在现有的配置字段用尽时，提供额外的事件过滤控制。

2. **之前讨论要点**：在历史讨论中，James 提到补丁 v9 的更新包括修复文档中的拼写错误，并且重新基于最新的 perf-tools-next。Will Deacon 请求核心 perf 维护者对扩展功能进行确认或拒绝。

3. **本周的新讨论与进展**：本周的讨论中，Peter Zijlstra 对 `config4` 字段的必要性提出质疑，认为现有的字段仍有空间可用。James 解释了数据源和过滤器之间的区别，强调过滤器的 64 位设计允许对多个数据源进行位操作过滤。最终，Peter 表示理解并确认了补丁，表示支持。Will Deacon 也对补丁表示认可。

总体来看，讨论围绕补丁的必要性和实现细节展开，最终达成了一致意见，推动了补丁的进展。

#### 📝 邮件列表

1. **[10-29 15:46]** [PATCH v9 0/5] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[10-29 15:46]** [PATCH v9 1/5] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
3. **[10-29 15:46]** [PATCH v9 2/5] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
4. **[11-03 14:33]** Re: [PATCH v9 1/5] perf: Add perf_event_attr::config4
   - 发件人: Will Deacon <will@kernel.org>
5. **[11-10 16:48]** Re: [PATCH v9 2/5] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: Peter Zijlstra <peterz@infradead.org>
6. **[11-11 10:51]** Re: [PATCH v9 2/5] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
7. **[11-11 11:55]** Re: [PATCH v9 2/5] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: Peter Zijlstra <peterz@infradead.org>
8. **[11-11 11:55]** Re: [PATCH v9 1/5] perf: Add perf_event_attr::config4
   - 发件人: Peter Zijlstra <peterz@infradead.org>

---

### Thread 11: [PATCH v2 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 30 Oct 2025 12:27:04 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 ID_PFR1_EL1.GIC 的处理进行修复的补丁系列。历史讨论中，Marc Zyngier 提到 Peter 报告了在恢复 GICv2 虚拟机时出现的问题，指出 ID_PFR1_EL1.GIC 不是可写的，而其 64 位等价物是可写的，这一问题在 6.12 版本中引入。补丁旨在修复这些问题，并确保在创建 GIC 时调整 ID 寄存器。

在本周的新讨论中，Mark Brown 提出了在多个物理 arm64 平台上（包括 A53、A55 和 A72 系统）出现的回归问题，导致在 ID 寄存器设置时出现内核警告。经过 bisect 测试，确认了补丁的影响。Marc Zyngier 进一步指出，问题主要出现在 GICv2 平台上，而 GICv3 平台似乎没有问题。最终，讨论中提出了一种临时修复方法，Marc 和 Mark 都表示在他们测试的设备上，这种修复有效。

总结来说，此次讨论集中在修复 KVM 对 ID_PFR1_EL1.GIC 的处理问题上，虽然补丁引入了一些回归问题，但通过社区的共同努力，找到了解决方案。

#### 📝 邮件列表

1. **[10-30 12:27]** [PATCH v2 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[10-30 12:27]** [PATCH v2 3/3] KVM: arm64: Limit clearing of ID_{AA64PFR0,PFR1}_EL1.GIC to userspace irqchip
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-10 12:51]** Re: [PATCH v2 3/3] KVM: arm64: Limit clearing of
 ID_{AA64PFR0,PFR1}_EL1.GIC to userspace irqchip
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[11-10 13:11]** Re: [PATCH v2 3/3] KVM: arm64: Limit clearing of ID_{AA64PFR0,PFR1}_EL1.GIC to userspace irqchip
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[11-10 14:15]** Re: [PATCH v2 3/3] KVM: arm64: Limit clearing of
 ID_{AA64PFR0,PFR1}_EL1.GIC to userspace irqchip
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[11-10 14:29]** Re: [PATCH v2 3/3] KVM: arm64: Limit clearing of ID_{AA64PFR0,PFR1}_EL1.GIC to userspace irqchip
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[11-10 17:20]** Re: [PATCH v2 3/3] KVM: arm64: Limit clearing of
 ID_{AA64PFR0,PFR1}_EL1.GIC to userspace irqchip
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 12: [PATCH v10 0/5] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 11 Nov 2025 11:37:54 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARMv8.8 SPE 特性的补丁（PATCH v10 0/5），主要集中在数据源过滤功能的支持上。补丁的核心内容是引入了一种新的数据源过滤机制（SPE_FEAT_FDS），允许通过一个新的配置字段（config4）来过滤数据包的来源。

在历史讨论中，补丁经历了多个版本的迭代，逐步修正了文档中的错误，优化了代码结构，并在每个版本中添加了对新特性的支持。特别是在 v4 版本中，补丁引入了数据源过滤的反转逻辑，使得默认值为 0 时包含所有数据源，从而简化了配置。

本周的新讨论中，James Clark 提交了补丁的最终版本，详细说明了 config4 字段的添加及其在数据源过滤中的应用。此外，补丁还更新了相关文档，详细描述了新特性及其使用方法，确保用户能够理解如何利用这些新功能进行性能监控。

总的来说，本周的进展主要集中在补丁的最终确认和文档的完善上，确保新特性能够顺利集成到 Linux 内核中。

#### 📝 邮件列表

1. **[11-11 11:37]** [PATCH v10 0/5] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[11-11 11:37]** [PATCH v10 1/5] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
3. **[11-11 11:37]** [PATCH v10 2/5] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
4. **[11-11 11:37]** [PATCH v10 3/5] tools headers UAPI: Sync linux/perf_event.h with
 the kernel sources
   - 发件人: James Clark <james.clark@linaro.org>
5. **[11-11 11:37]** [PATCH v10 4/5] perf tools: Add support for
 perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
6. **[11-11 11:37]** [PATCH v10 5/5] perf docs: arm-spe: Document new SPE filtering
 features
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 13: [PATCH v3 0/2]  arm: add kvm-psci-version vcpu property

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 12 Nov 2025 19:13:55 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM 架构的 KVM 相关补丁，主题为增加 `kvm-psci-version` vcpu 属性，以便支持在不同默认 PSCI 版本的主机内核之间进行迁移。

**原始补丁内容**：
该补丁系列的目的是通过 KVM 注册 `KVM_REG_ARM_PSCI_VERSION`，为 vcpu 提供一个选项，以请求特定的 PSCI 版本。当前支持的版本包括 0.1、0.2、1.0、1.1、1.2 和 1.3。

**之前讨论要点**：
在之前的讨论中，开发者们关注如何处理不同 PSCI 版本的兼容性问题，特别是支持 PSCI v0.1 时需要放弃对 KVM_CAP_ARM_PSCI_0_2 的初始化。此外，补丁经过多次修改，吸收了社区成员的反馈。

**本周新讨论与进展**：
本周的讨论主要集中在补丁的实现细节上。Sebastian Ott 提出了补丁的更新，修复了 `kvm_get_psci_version()` 函数的问题，并添加了对新 PSCI 版本的常量定义。Philippe Mathieu-Daudé 建议在代码中枚举可用的 PSCI 版本，Sebastian 则认为可以简化描述，建议使用更简洁的表达方式。整体来看，补丁的开发进展顺利，社区成员积极参与讨论，提出了建设性的意见。

#### 📝 邮件列表

1. **[11-12 19:13]** [PATCH v3 0/2]  arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[11-12 19:13]** [PATCH v3 1/2] target/arm/kvm: add constants for new PSCI versions
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[11-12 19:13]** [PATCH v3 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[11-12 22:07]** Re: [PATCH v3 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: =?UTF-8?Q?Philippe_Mathieu-Daud=C3=A9?= <philmd@linaro.org>
5. **[11-13 13:05]** Re: [PATCH v3 2/2] target/arm/kvm: add kvm-psci-version vcpu
 property
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 14: [PATCH 0/3] KVM: arm64: Reschedule as needed when destroying the
 stage-2 page-tables

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 13 Nov 2025 05:24:49 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在处理 ARM64 架构时，销毁阶段 2 页表时的调度问题。

1. **原始 patch/问题的内容**：
   讨论的核心是当一个完全映射的 128G 虚拟机被突然销毁时，系统会出现调度警告，提示 CPU 在超过 100 毫秒内未被调度。这是因为在没有强制抢占的内核配置下，页表遍历操作耗时过长。

2. **之前的讨论要点**：
   为了解决这个问题，提议将页表遍历操作拆分为更小的范围，并在每个范围之间检查 `cond_resched()`，以便在长时间操作时能够适时让出 CPU。之前的补丁曾被合并，但由于发现了使用后释放（UAF）漏洞而被撤回。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，参与者提出了三个补丁：
   - **补丁 1**：在 `stage2_free_walker()` 中，只有在表为空时才释放引用。
   - **补丁 2**：将 `kvm_pgtable_stage2_destroy()` 拆分为两个函数，以便在处理大页表时能够分块进行。
   - **补丁 3**：实现了在销毁阶段 2 页表时定期调用 `cond_resched()`，以避免长时间占用 CPU。所有补丁的目的是解决之前的调度警告问题，并确保在处理大规模页表时系统的响应性。

#### 📝 邮件列表

1. **[11-13 05:24]** [PATCH 0/3] KVM: arm64: Reschedule as needed when destroying the
 stage-2 page-tables
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[11-13 05:24]** [PATCH 1/3] KVM: arm64: Only drop references on empty tables in stage2_free_walker
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
3. **[11-13 05:24]** [PATCH 2/3] KVM: arm64: Split kvm_pgtable_stage2_destroy()
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
4. **[11-13 05:24]** [PATCH 3/3] KVM: arm64: Reschedule as needed when destroying the
 stage-2 page-tables
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>

---

### Thread 15: [PATCH] KVM: arm64: VHE: Compute fgt traps before activating them

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 12 Nov 2025 10:28:53 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在解决在激活细粒度陷阱（Fine Grain Traps, FGT）之前计算 FGT 的问题。

**原始补丁内容**：
补丁的主要内容是修复在 VHE（Virtualization Host Extensions）环境中，FGT 寄存器在第一次加载 VCPU 时可能会写入零值的问题。补丁通过在将 FGT 陷阱写入硬件之前计算 FGT 数组来解决这一问题。

**之前讨论要点**：
在历史讨论中并没有具体的内容，但补丁的背景是由于在运行 Linux 客户机时，FGT 寄存器的值未能及时更新，导致了潜在的错误。

**本周的新讨论与进展**：
本周的讨论中，Alexandru Elisei 提出了补丁并详细描述了问题及其解决方案。Oliver Upton 对补丁进行了审查并表示认可，认为补丁解决了一个重要问题。Marc Zyngier 则确认已将补丁应用到修复分支中。最后，Alexandru 和 Oliver 讨论了函数命名的问题，确认命名与现有约定一致，未造成混淆。

综上所述，该补丁已被接受并应用，解决了 VHE 环境下 FGT 寄存器初始化不当的问题。

#### 📝 邮件列表

1. **[11-12 10:28]** [PATCH] KVM: arm64: VHE: Compute fgt traps before activating them
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[11-12 02:40]** Re: [PATCH] KVM: arm64: VHE: Compute fgt traps before activating them
   - 发件人: Oliver Upton <oupton@kernel.org>
3. **[11-12 10:54]** Re: [PATCH] KVM: arm64: VHE: Compute fgt traps before activating them
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[11-12 10:56]** Re: [PATCH] KVM: arm64: VHE: Compute fgt traps before activating them
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 16: [PATCH] KVM: selftests: Add SYNC after guest ITS setup in vgic_lpi_stress

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 14 Nov 2025 15:39:02 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 自测试中的一个补丁，旨在确保在进行虚拟化中断处理时，ITS（中断转发系统）映射完成后再进行 LPI（本地中断）注入。

1. **原始补丁内容**：补丁的核心是添加一个 SYNC 命令，以确保在调用 KVM_SIGNAL_MSI 注入 LPI 之前，ITS 的映射命令已完成。这是为了遵循 ARM 架构规范，避免因实现细节而导致的潜在错误。

2. **之前的讨论要点**：补丁的提出者 Maximilian Dittgen 指出，虽然 KVM 实际上是同步处理 ITS 命令的，因此在功能上 SYNC 调用是多余的，但自测试应遵循架构规范，而非依赖于 KVM 的实现优化。

3. **本周的新讨论与进展**：本周的讨论中，Marc Zyngier 对补丁中的某些实现假设提出了质疑，认为补丁中提到的处理器编号与 CPU 编号的假设并不符合架构规范。Oliver Upton 则建议在 GIC 初始化中添加断言，以确保处理器编号与 CPU 一致。整体来看，讨论集中在如何确保自测试的架构合规性与实现细节之间的平衡。

#### 📝 邮件列表

1. **[11-14 15:39]** [PATCH] KVM: selftests: Add SYNC after guest ITS setup in vgic_lpi_stress
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
2. **[11-14 15:42]** Re: [PATCH] KVM: selftests: Add SYNC after guest ITS setup in vgic_lpi_stress
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-14 12:26]** Re: [PATCH] KVM: selftests: Add SYNC after guest ITS setup in
 vgic_lpi_stress
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 17: [PATCH V6 1/3] tools: header: arm64: Replace TCR_NFD[0|1] with
 TCR_EL1_NFD[0|1]

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 3 Nov 2025 17:31:27 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（patch）——“[PATCH V6 1/3] tools: header: arm64: 替换 TCR_NFD[0|1] 为 TCR_EL1_NFD[0|1]”。该补丁旨在更新 ARM64 架构的工具头文件，以反映内核中的最新更改。

在历史讨论中，参与者 Catalin Marinas 和 Leo Yan 提到，通常这些头文件是通过脚本自动同步更新的，主要由 perf 工具的维护者负责。Leo 还表示，他在构建 perf 时没有遇到任何问题，并认为发送该补丁是合理的。他建议在内核更改合并后提醒 perf 维护者，以确保工具中的更改安全地被采纳。

在本周的新讨论中，Anshuman Khandual 对之前的观点表示赞同，并确认他也没有发现任何问题。这表明参与者们对补丁的接受度较高，并且在技术上没有阻碍。

总体来看，该补丁得到了积极的反馈，参与者们一致认为可以继续推进这一更改。

#### 📝 邮件列表

1. **[11-03 17:31]** Re: [PATCH V6 1/3] tools: header: arm64: Replace TCR_NFD[0|1] with
 TCR_EL1_NFD[0|1]
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
2. **[11-03 18:03]** Re: [PATCH V6 1/3] tools: header: arm64: Replace TCR_NFD[0|1] with
 TCR_EL1_NFD[0|1]
   - 发件人: Leo Yan <leo.yan@arm.com>
3. **[11-13 14:39]** Re: [PATCH V6 1/3] tools: header: arm64: Replace TCR_NFD[0|1] with
 TCR_EL1_NFD[0|1]
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 18: [PATCH] KVM: arm64: add missing newline to sysreg init log

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 10 Nov 2025 23:10:51 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在为系统寄存器初始化日志添加缺失的换行符。该补丁的主要目的是改善控制台输出的格式，确保日志信息不会与后续日志合并，尽管这项更改不会影响系统的行为。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出补丁的提出是为了提高日志的可读性。Osama Abdelkader 提出了这个补丁，并在邮件中说明了其目的。

在本周的新讨论中，Osama 提交了补丁后，Marc Zyngier 对此表示质疑，认为在 `kvm_sys_reg_table_init()` 函数中已经有足够的错误提示，因此不需要额外的日志信息。最终，Osama 采纳了 Marc 的建议，决定撤回该补丁，去掉这条日志信息。整体来看，本周的讨论集中在日志信息的必要性和可读性上，最终决定不实施补丁。

#### 📝 邮件列表

1. **[11-10 23:10]** [PATCH] KVM: arm64: add missing newline to sysreg init log
   - 发件人: Osama Abdelkader <osama.abdelkader@gmail.com>
2. **[11-11 09:49]** Re: [PATCH] KVM: arm64: add missing newline to sysreg init log
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-11 20:54]** Re: [PATCH] KVM: arm64: add missing newline to sysreg init log
   - 发件人: Osama Abdelkader <osama.abdelkader@gmail.com>

---

### Thread 19: [PATCH] KVM: arm64: Finalize ID registers only once per VM

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 10 Nov 2025 17:30:10 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在确保每个虚拟机（VM）只对 ID 寄存器进行一次最终化处理。

**原始补丁内容**：补丁提出了一个问题，即 ID 寄存器是全局于 VM 的，因此不应重复计算。最近的更改导致在不必要的情况下频繁更新 ID 寄存器。补丁通过在 VM 从未运行的情况下才更新 ID 寄存器来解决这一问题。

**之前的讨论要点**：由于本邮件线程没有历史讨论部分，无法提供之前讨论的具体要点。

**本周的新讨论与进展**：本周的讨论中，Marc Zyngier 提交了补丁，并指出该补丁解决了他在测试中遇到的所有问题。Mark Brown 也确认了补丁的有效性，并表示已成功测试。最终，Marc Zyngier 确认补丁已被应用到修复列表中。

总结而言，此次讨论集中在优化 KVM 的 ID 寄存器处理上，通过补丁确保每个 VM 只进行一次寄存器最终化，提升了系统的效率和稳定性。

#### 📝 邮件列表

1. **[11-10 17:30]** [PATCH] KVM: arm64: Finalize ID registers only once per VM
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-11 12:04]** Re: [PATCH] KVM: arm64: Finalize ID registers only once per VM
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[11-11 12:25]** Re: [PATCH] KVM: arm64: Finalize ID registers only once per VM
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 20: [PATCH] KVM: arm64: GICv3: Don't advertise ICH_HCR_EL2.En==1 when no vgic is configured

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 14 Nov 2025 09:35:41 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下对 GICv3（通用中断控制器版本3）的配置问题。Marc Zyngier 提出的补丁旨在解决在未配置 vgic（虚拟中断控制器）的情况下，错误地将 ICH_HCR_EL2.En 设置为 1 的问题。该补丁确保在没有 vgic 的情况下，不会修改 vgic_hcr，从而避免在来宾系统中触发未定义的行为。

在历史讨论中，补丁的背景是为了修复之前的一个问题，该问题源于对 vgic 维护中断配置的重构（提交 ID: 877324a1b5415）。Marc Zyngier 在补丁中指出，配置 GICv3 时，必须确保不设置 ICH_HCR_EL2.En，以便能够捕获所有系统寄存器并在来宾中报告未定义的行为。

在本周的新讨论中，Marc Zyngier 提交了补丁并得到了 Mark Brown 的测试反馈，确认该补丁解决了在没有 vgic-v3 的情况下出现的问题。Mark Brown 也表示支持该补丁的修改。整体来看，本周的讨论主要集中在补丁的有效性和测试结果上，显示出对该问题的积极解决态度。

#### 📝 邮件列表

1. **[11-14 09:35]** [PATCH] KVM: arm64: GICv3: Don't advertise ICH_HCR_EL2.En==1 when no vgic is configured
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-14 15:04]** Re: [PATCH] KVM: arm64: GICv3: Don't advertise ICH_HCR_EL2.En==1
 when no vgic is configured
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 21: [PATCH] KVM: arm64: GICv3: Check the implementation before accessing ICH_VTR_EL2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 13 Nov 2025 17:25:24 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 GICv3（通用中断控制器版本3）的实现进行检查，以确保在访问 ICH_VTR_EL2 寄存器之前确认硬件的兼容性。

**原始 patch/问题的内容**：
Marc Zyngier 提出的 patch 旨在修复在某些硬件上访问 ICH_VTR_EL2 时可能导致的未定义行为（UNDEF）。该 patch 通过在读取 ICH_VTR_EL2 寄存器之前检查当前运行的硬件是否为 GICv3，从而避免在不支持该寄存器的硬件上引发问题。

**之前讨论要点**：
在历史讨论中，虽然没有具体的邮件记录，但可以推测之前的讨论集中在如何处理不同硬件实现的兼容性问题，尤其是 Apple 硬件的特殊情况。

**本周的新讨论、进展或结论**：
本周的讨论中，Marc Zyngier 提交了该 patch，并得到了 Marek Szyprowski 的测试反馈。Oliver Upton 对该 patch 表示感谢，并确认已将其应用到下一个版本中。这表明该 patch 已经获得认可，并将进一步整合到 KVM 的代码库中。

#### 📝 邮件列表

1. **[11-13 17:25]** [PATCH] KVM: arm64: GICv3: Check the implementation before accessing ICH_VTR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-13 13:37]** Re: [PATCH] KVM: arm64: GICv3: Check the implementation before accessing ICH_VTR_EL2
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 22: [PATCH] arm64: Fix double word in comments

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 29 Oct 2025 15:17:42 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 ARM64 架构的一个补丁，旨在修复代码注释中的重复单词“the”。该补丁由 Bo Liu 提出，涉及两个文件的修改，具体为在 `entry-ftrace.S` 和 `arm.c` 文件中删除了重复的单词。

在历史讨论中，Bo Liu 提出了这个补丁，并详细说明了其修改内容，强调了代码注释的清晰性和准确性的重要性。该补丁的签名也表明了其作者的身份。

在本周的新讨论中，Catalin Marinas 确认了该补丁已被应用到 ARM64 的代码库中，并表示感谢。这表明该补丁得到了认可，并已正式合并到相关代码分支中，进一步提升了代码的可读性。

总结来说，此次讨论主要集中在一个小的代码修正上，虽然内容简单，但反映了开发者对代码质量的重视。

#### 📝 邮件列表

1. **[10-29 15:17]** [PATCH] arm64: Fix double word in comments
   - 发件人: Bo Liu <liubo03@inspur.com>
2. **[11-12 18:33]** Re: [PATCH] arm64: Fix double word in comments
   - 发件人: Catalin Marinas <cmarinas@kernel.org>

---

### Thread 23: [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 30 Oct 2025 13:09:23 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 x86 架构下的 TDX（Trusted Domain Extensions）后填充清理的补丁集，共包含 28 个补丁。

在历史讨论中，Sean Christopherson 提出了该补丁集的背景，主要针对 KVM 的 TDX 后填充路径进行清理，以解决 gmem 和 TDX 后填充钩子之间的锁定问题，以及 KVM 内部的互斥性问题。补丁的前两部分引入了对 `kvm_arch_vcpu_async_ioctl()` 的强制要求，并将其重命名为 `kvm_arch_vcpu_unlocked_ioctl()`，这对非 x86 用户可能更具吸引力。

在本周的新讨论中，Sean Christopherson 更新了补丁集，表示已将其应用于 kvm-x86 的 TDX 分支，并对各种拼写错误进行了修正。同时，他感谢了所有参与审查和测试的人员，并邀请其他 KVM 架构维护者，如果需要，可以请求为 `kvm_arch_vcpu_async_ioctl()` 的更改提供稳定标签。

总结来看，该讨论主要集中在 KVM 的 TDX 后填充清理补丁的应用与审查进展上，强调了代码的可维护性和稳定性。

#### 📝 邮件列表

1. **[10-30 13:09]** [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[11-10 07:37]** Re: [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 24: [PATCH v4] arm64: errata: Work around AmpereOne's erratum
 AC04_CPU_23

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 16 Nov 2025 16:31:04 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于针对 AmpereOne AC04 系统的 erratum AC04_CPU_23 的补丁（PATCH v4）。该补丁旨在解决 AmpereOne AC04 系统中的特定问题，通过启用相应的工作绕过措施来应对该错误。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是基于对 AmpereOne AC04 系统的错误分析，目的是确保系统的稳定性和性能。

在本周的新讨论中，参与者 Jaikiran Pai 向补丁的作者 D Scott Phillips 提出了一个问题，询问该补丁是否仅针对 AmpereOne AC04 系统，还是也可能影响到 AmpereOne AC03 系统。他提到 AC03 系统的 CPU 相关信息，暗示可能存在类似的问题需要关注。这表明对于补丁的适用性和潜在影响，讨论仍在继续，尚未得出明确结论。

#### 📝 邮件列表

1. **[11-16 16:31]** Re: [PATCH v4] arm64: errata: Work around AmpereOne's erratum
 AC04_CPU_23
   - 发件人: Jaikiran Pai <jai.forums2013@gmail.com>

---

### Thread 25: [PATCH] KVM: arm64: Fix error checking for FFA_VERSION

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 14 Nov 2025 11:11:53 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 FFA_VERSION 的错误检查逻辑。

1. **原始 patch/问题的内容**：补丁的主要内容是修复在处理 FF-A（Firmware Framework for Arm）版本时的错误检查逻辑。根据 DEN0077 FF-A 规范第 13.2 节，当固件不支持请求的版本时，应返回 FFA_RET_NOT_SUPPORTED（-1）。目前的实现中，错误检查逻辑将从 SMC（Secure Monitor Call）层返回的无符号长整型值与“-1”进行比较，导致类型不匹配，从而错误地将“-1”解释为无效的 FF-A 版本，进而阻止了在不支持 FF-A 的固件设备上进行 pKVM 初始化。

2. **之前的讨论要点**：由于本邮件线程没有历史讨论，因此没有相关的背景信息。

3. **本周的新讨论、进展或结论**：本周的讨论由 Kornel Dulęba 提出，详细说明了问题的根源及其解决方案，即通过将返回值显式转换为有符号整型（s32）来修复错误检查逻辑。补丁已包含在邮件中，并对相关代码进行了修改，以确保在 FF-A 不支持时能够正确处理返回值。

总的来说，该补丁解决了 KVM 在 arm64 架构下与 FF-A 版本检查相关的一个关键问题，确保了在固件不支持 FF-A 的情况下，pKVM 能够正常初始化。

#### 📝 邮件列表

1. **[11-14 11:11]** [PATCH] KVM: arm64: Fix error checking for FFA_VERSION
   - 发件人: =?utf-8?q?Kornel_Dul=C4=99ba?= <korneld@google.com>

---

### Thread 26: [PATCH v5 44/44] KVM: x86/pmu: Elide WRMSRs when loading guest
 PMCs if values already match

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 14 Nov 2025 11:49:30 +0530

#### 🤖 AI 总结

本邮件主题为“[PATCH v5 44/44] KVM: x86/pmu: Elide WRMSRs when loading guest PMCs if values already match”，主要涉及在加载虚拟机性能监控计数器（PMCs）时，如果值已经匹配，则省略写入MSR（模型特定寄存器）的操作。

在本周的新讨论中，参与者Manali Shukla对之前的补丁内容提出了一个小的修正意见，指出文中提到的“AMD Turing”应更正为“AMD Turin”。这表明在补丁的描述中存在一些术语上的不准确，需要进行修正。

由于本邮件列表没有提供更多的历史讨论内容，因此无法总结之前的讨论要点。当前的讨论主要集中在补丁的细节修正上，未涉及更广泛的技术问题或争议。整体来看，本周的进展主要是对补丁描述的细微调整，未对补丁的核心内容产生实质性影响。

#### 📝 邮件列表

1. **[11-14 11:49]** Re: [PATCH v5 44/44] KVM: x86/pmu: Elide WRMSRs when loading guest
 PMCs if values already match
   - 发件人: Manali Shukla <manali.shukla@amd.com>

---

### Thread 27: [PATCH 00/10] KVM: selftests: Convert to kernel-style types

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 13 Nov 2025 16:52:25 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 自测工具的一个补丁（PATCH 00/10），目的是将其转换为内核风格的类型。该补丁的提出旨在提高代码的一致性和可读性。

在之前的讨论中，参与者对补丁的内容表示支持，特别是对类型重命名的提议。然而，关于补丁的提交时机和协调问题，参与者们存在一些顾虑。David Matlack 提到，若能在 6.18 版本中提交该补丁，将有助于避免与最新 LTS 版本的冲突。他建议可以考虑重新生成补丁，并寻求 Paolo 的帮助，在下一个合并窗口结束时应用该补丁，并将其标记为稳定版本，以减少后续的维护问题。

本周的讨论主要集中在补丁的提交策略上，虽然参与者对补丁本身持积极态度，但在具体实施时仍需进一步协调和规划。

#### 📝 邮件列表

1. **[11-13 16:52]** Re: [PATCH 00/10] KVM: selftests: Convert to kernel-style types
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 28: (subset) [PATCH v3 0/5] arm64/sysreg: Introduce Prefix descriptor and generated ICH_VMCR_EL2 support

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 13 Nov 2025 19:01:00 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 系统寄存器的补丁（PATCH v3 0/5），主要引入了前缀描述符和生成的 ICH_VMCR_EL2 支持。

在历史讨论中，补丁的内容包括五个部分：首先是修复不完整的 sysreg 定义检查，其次是支持带有“Prefix”描述符的特征特定字段，接着将 RES0/RES1/UNKN 的生成移动到函数中，最后添加了 ICH_VMCR_EL2。该补丁旨在增强 ARM64 架构的系统寄存器功能。

本周的新讨论中，参与者 Catalin Marinas 确认了补丁已被应用到 arm64 的 for-next/sysreg 分支，并感谢 Sascha Bischoff 的贡献。补丁的前四部分已经得到处理，而最后一部分则留给 Marc 和 Oliver 进行进一步的审查和处理。

总的来说，本周的讨论确认了补丁的进展，并为后续的工作指明了方向。

#### 📝 邮件列表

1. **[11-13 19:01]** Re: (subset) [PATCH v3 0/5] arm64/sysreg: Introduce Prefix descriptor and generated ICH_VMCR_EL2 support
   - 发件人: Catalin Marinas <cmarinas@kernel.org>

---

### Thread 29: (subset) [PATCH V6 0/3] arm64/sysreg: Clean up TCR_EL1 field macros

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 13 Nov 2025 18:59:34 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于对 ARM64 架构中 TCR_EL1 字段宏的清理工作，具体内容为一系列补丁（PATCH V6 0/3）。该补丁旨在简化和优化 TCR_EL1 字段的宏定义，以提高代码的可读性和维护性。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁是基于之前对 ARM64 系统寄存器的讨论，旨在解决宏定义的复杂性问题。

在本周的新讨论中，参与者 Catalin Marinas 确认已将补丁应用于 arm64 的开发分支（for-next/sysreg），并感谢 Anshuman Khandual 的贡献。补丁中的第二个部分（[2/3]）涉及替换 TCR_EL1 字段宏的具体实现，相关代码可以在提供的链接中查看。此外，Catalin 提到工具头文件的更新可以在后续进行，但目前尚未排入日程，同时将 KVM 相关的更改留给其他开发者（Marc 和 Oliver）处理。

总体而言，本周的讨论主要集中在补丁的应用和后续工作的安排上，标志着该项目的进展。

#### 📝 邮件列表

1. **[11-13 18:59]** Re: (subset) [PATCH V6 0/3] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Catalin Marinas <cmarinas@kernel.org>

---

### Thread 30: [PATCH V2 0/2] arm64/mm: Add remaining TLBI_XXX_MASK macros

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 13 Nov 2025 14:45:12 +0530

#### 🤖 AI 总结

本邮件线程讨论了一个针对 arm64 架构的补丁，主题为“[PATCH V2 0/2] arm64/mm: Add remaining TLBI_XXX_MASK macros”。该补丁的目的是添加剩余的 TLBI（Translation Lookaside Buffer Invalid）宏，以增强内存管理的功能。

在历史讨论中，虽然没有具体的内容记录，但可以推测该补丁是为了完善 arm64 架构下的内存管理机制，确保所有必要的 TLBI 宏都被定义和实现。

在本周的新讨论中，参与者 Anshuman Khandual 对补丁进行了跟进，询问是否有任何更新或对这些更改的关注。他的邮件表明该补丁尚未得到明确的反馈，显示出对进展的关注。

总体来看，该补丁旨在改进 arm64 的内存管理，当前仍在等待社区的反馈和进一步的讨论。

#### 📝 邮件列表

1. **[11-13 14:45]** Re: [PATCH V2 0/2] arm64/mm: Add remaining TLBI_XXX_MASK macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 31: [PATCH] KVM: arm64:  drop sysreg init error log

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 11 Nov 2025 20:50:05 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的一个补丁，主要内容是删除系统寄存器初始化过程中的错误日志记录。

**原始 patch/问题的内容**：
该补丁由 Osama Abdelkader 提出，目的是在 `kvm_sys_reg_table_init()` 函数中，去除冗余的错误信息输出。当前的实现已经在失败路径中发出了过多的错误信息，因此在调用者处的额外 `kvm_info()` 输出显得多余。

**之前讨论要点**：
由于本邮件线程中没有历史讨论，因此没有之前的讨论要点。

**本周的新讨论、进展或结论**：
在本周的讨论中，Osama Abdelkader 提出了具体的代码修改建议，删除了在系统寄存器表初始化失败时的冗余日志输出。补丁的具体实现是对 `arch/arm64/kvm/arm.c` 文件进行了修改，减少了错误信息的输出行数，从而使代码更加简洁。此补丁已被提交，等待进一步的审查和反馈。

#### 📝 邮件列表

1. **[11-11 20:50]** [PATCH] KVM: arm64:  drop sysreg init error log
   - 发件人: Osama Abdelkader <osama.abdelkader@gmail.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH v6 00/35] KVM: arm64: Add Statistical Profiling Extension (SPE) support

**📧 邮件数**: 36 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 14 Nov 2025 16:06:41 +0000

#### 🤖 AI 总结

本邮件线程讨论了对 KVM（Kernel-based Virtual Machine）在 arm64 架构上添加统计分析扩展（SPE）支持的补丁系列（RFC PATCH v6 00/35）。该补丁旨在解决在虚拟机中使用 SPE 时，因内存映射和翻译故障导致的采样中断问题。

1. **原始补丁内容**：补丁系列主要包括对 SPE 的支持，允许在虚拟机中启用统计分析功能。补丁中涉及到的关键注册表包括 PMBLIMITR_EL1、PMBPTR_EL1 和 PMBSR_EL1，这些注册表控制着 SPE 缓冲区的行为。

2. **历史讨论要点**：之前的讨论集中在如何有效地管理 SPE 缓冲区的内存映射，确保在虚拟机运行时不会出现采样中断的“黑窗”现象。补丁提出了通过在主机上固定与缓冲区对应的页面，并在第二阶段映射这些页面来解决此问题。

3. **本周的新讨论与进展**：本周的讨论主要集中在补丁的具体实现细节上，包括如何处理 MMU 通知、如何在 VCPU 加载和退出时保存和恢复 SPE 状态、以及如何确保在内存不足时适当地处理 RLIMIT_MEMLOCK 限制。此外，补丁还增加了对 hugetlb 页的支持，确保在使用 hugetlb 页时不会引发额外的翻译故障。最后，补丁允许用户空间创建启用 SPE 的虚拟机。

整体而言，该补丁系列为 KVM 的 SPE 支持奠定了基础，解决了多个潜在问题，并为未来的优化和功能扩展提供了可能性。

#### 📝 邮件列表

1. **[11-14 16:06]** [RFC PATCH v6 00/35] KVM: arm64: Add Statistical Profiling Extension (SPE) support
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[11-14 16:06]** [RFC PATCH v6 01/35] arm64/sysreg: Add new SPE fields
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[11-14 16:06]** [RFC PATCH v6 02/35] arm64/sysreg: Define MDCR_EL2.E2PB values
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[11-14 16:06]** [RFC PATCH v6 03/35] KVM: arm64: Add CONFIG_KVM_ARM_SPE Kconfig option
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
5. **[11-14 16:06]** [RFC PATCH v6 04/35] perf: arm_spe_pmu: Move struct arm_spe_pmu to a separate header file
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[11-14 16:06]** [RFC PATCH v6 05/35] KVM: arm64: Add KVM_CAP_ARM_SPE capability
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[11-14 16:06]** [RFC PATCH v6 06/35] KVM: arm64: Add KVM_ARM_VCPU_SPE VCPU feature
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[11-14 16:06]** [RFC PATCH v6 07/35] HACK! KVM: arm64: Disable SPE virtualization if protected KVM is enabled
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
9. **[11-14 16:06]** [RFC PATCH v6 08/35] HACK! KVM: arm64: Enable SPE virtualization only in VHE mode
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
10. **[11-14 16:06]** [RFC PATCH v6 09/35] HACK! KVM: arm64: Disable SPE virtualization if nested virt is enabled
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
11. **[11-14 16:06]** [RFC PATCH v6 10/35] KVM: arm64: Add a new VCPU device control group for SPE
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
12. **[11-14 16:06]** [RFC PATCH v6 11/35] KVM: arm64: Add SPE VCPU device attribute to set the interrupt number
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
13. **[11-14 16:06]** [RFC PATCH v6 12/35] KVM: arm64: Add SPE VCPU device attribute to set the SPU device
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
14. **[11-14 16:06]** [RFC PATCH v6 13/35] perf: arm_spe_pmu: Add PMBIDR_EL1 to struct arm_spe_pmu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
15. **[11-14 16:06]** [RFC PATCH v6 14/35] KVM: arm64: Add SPE VCPU device attribute to set the max buffer size
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
16. **[11-14 16:06]** [RFC PATCH v6 15/35] KVM: arm64: Add SPE VCPU device attribute to initialize SPE
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
17. **[11-14 16:06]** [RFC PATCH v6 16/35] KVM: arm64: Advertise SPE version in ID_AA64DFR0_EL1.PMSver
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
18. **[11-14 16:06]** [RFC PATCH v6 17/35] KVM: arm64: Add writable SPE system registers to VCPU context
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
19. **[11-14 16:06]** [RFC PATCH v6 18/35] perf: arm_spe_pmu: Add PMSIDR_EL1 to struct arm_spe_pmu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
20. **[11-14 16:07]** [RFC PATCH v6 19/35] KVM: arm64: Trap PMBIDR_EL1 and PMSIDR_EL1
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
21. **[11-14 16:07]** [RFC PATCH v6 20/35] KVM: arm64: config: Use functions from spe.c to test FEAT_SPE_{FnE,FDS}
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
22. **[11-14 16:07]** [RFC PATCH v6 21/35] KVM: arm64: Check for unsupported CPU early in kvm_arch_vcpu_load()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
23. **[11-14 16:07]** [RFC PATCH v6 22/35] KVM: arm64: VHE: Context switch SPE state
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
24. **[11-14 16:07]** [RFC PATCH v6 23/35] KVM: arm64: Allow guest SPE physical timestamps only if perfmon_capable()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
25. **[11-14 16:07]** [RFC PATCH v6 24/35] KVM: arm64: Handle SPE hardware maintenance interrupts
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
26. **[11-14 16:07]** [RFC PATCH v6 25/35] KVM: arm64: Add basic handling of SPE buffer control registers writes
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
27. **[11-14 16:07]** [RFC PATCH v6 26/35] KVM: arm64: Add comment to explain how trapped SPE registers are handled
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
28. **[11-14 16:07]** [RFC PATCH v6 27/35] KVM: arm64: Make MTE functions public
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
29. **[11-14 16:07]** [RFC PATCH v6 28/35] KVM: arm64: at: Use callback for reading descriptor
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
30. **[11-14 16:07]** [RFC PATCH v6 29/35] KVM: arm64: Pin the SPE buffer in the host and map it at stage 2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
31. **[11-14 16:07]** [RFC PATCH v6 30/35] KVM: Propagate MMU event to the MMU notifier handlers
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
32. **[11-14 16:07]** [RFC PATCH v6 31/35] KVM: arm64: Handle MMU notifiers for the SPE buffer
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
33. **[11-14 16:07]** [RFC PATCH v6 32/35] KVM: Add KVM_EXIT_RLIMIT exit_reason
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
34. **[11-14 16:07]** [RFC PATCH v6 33/35] KVM: arm64: Implement locked memory accounting for the SPE buffer
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
35. **[11-14 16:07]** [RFC PATCH v6 34/35] KVM: arm64: Add hugetlb support for SPE
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
36. **[11-14 16:07]** [RFC PATCH v6 35/35] KVM: arm64: Allow the creation of a SPE enabled VM
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fix for 6.18, take #3

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 14 Nov 2025 11:34:15 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM/arm64 的修复补丁，旨在解决 6.18 版本中的一些回归问题。

1. **原始 patch/问题的内容**：本次补丁主要包括两个修复：一是确保在每次虚拟机运行时仅调整 ID 寄存器一次，而不是每个虚拟 CPU（vcpu）都调整一次，以避免在系统寄存器代码中触发严重的一致性检查失败；二是确保在加载硬件系统寄存器之前计算每个 vcpu 的细粒度陷阱（Fine Grain Traps），以避免在第一次 vcpu 的抢占之前运行时未设置任何内容。

2. **之前的讨论要点**：历史讨论部分没有提供具体内容，但可以推测之前的讨论涉及到 KVM/arm64 的一些回归问题，Marc Zyngier 在邮件中提到这些问题（如 FGT 问题）相当烦人，并希望此次修复能解决这些问题。

3. **本周的新讨论、进展或结论**：本周的讨论由 Marc Zyngier 提出，他回顾了收集补丁的常规工作，并请求 Paolo 拉取最新的修复补丁。他表示希望这次修复是本周期的最后一次，但内心仍有不安，认为可能还未完全解决所有问题。补丁已在 Git 仓库中可用，包含了对 ID 寄存器和细粒度陷阱计算的修复。

总体而言，本周的讨论集中在 KVM/arm64 的修复补丁上，旨在解决特定的回归问题，并希望能在即将发布的版本中得到解决。

#### 📝 邮件列表

1. **[11-14 11:34]** [GIT PULL] KVM/arm64 fix for 6.18, take #3
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Discussion

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 14 Nov 2025 16:58:39 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 单元测试的补丁（PATCH v2 0/4），旨在改善叶子函数的回溯信息。补丁包括四个部分：提供延迟 CFLAGS 的 Makefile 修改、针对 x86 和 arm64 的叶子函数回溯改进，以及修复涉及叶子函数的 arm 回溯问题。

在历史讨论中，Mathias Krause 提到补丁的 ARM 部分已获得 Andrew 和 Paolo 的认可，但由于 Paolo 对 KUT 的关注较少，Mathias 希望 Sean Christopherson 能够审查这些补丁。Sean 在本周的回复中确认了他会关注这些补丁，并表示之前未注意到这些内容。

本周的新进展包括 Sean 已将补丁应用到 kvm-x86 的下一版本中，并感谢 Mathias 的提醒。此外，Sean 还提到这促使他在自己的环境中使 pretty_print_stacks.py 工具正常工作。整体来看，讨论进展顺利，补丁得到了积极的反馈和应用。

#### 📝 邮件列表

1. **[11-14 16:58]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
2. **[11-14 08:39]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[11-14 10:25]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[11-15 05:56]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: [syzbot] [kvmarm?] WARNING in kvm_set_vm_id_reg

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 15 Nov 2025 10:59:20 -0800

#### 🤖 AI 总结

本邮件线程讨论了在 KVM (Kernel-based Virtual Machine) 的 ARM64 架构中，`kvm_set_vm_id_reg` 函数出现的警告问题。该问题由 syzbot 报告，涉及到在处理虚拟机 ID 寄存器时的错误，具体信息包括触发警告的代码位置和相关的调用栈。

在历史讨论中，虽然没有详细的背景信息，但可以推测该问题与 KVM 的 ARM64 实现有关，可能影响虚拟机的稳定性或功能。

在本周的新讨论中，syzbot 提供了详细的错误报告，包括内核版本、编译器信息和重现步骤。Marc Zyngier 对此问题作出了回应，提出了一个修复建议，建议在每个虚拟机中仅对 ID 寄存器进行一次最终化处理。这一建议表明开发者正在积极寻求解决方案，以确保 KVM 的正常运行。

总结而言，本周的讨论集中在 KVM ARM64 架构中的一个警告问题上，开发者们已经开始着手修复这一问题。

#### 📝 邮件列表

1. **[11-15 10:59]** [syzbot] [kvmarm?] WARNING in kvm_set_vm_id_reg
   - 发件人: syzbot <syzbot+c4aef6558d0cd90fe378@syzkaller.appspotmail.com>
2. **[11-16 08:46]** Re: [syzbot] [kvmarm?] WARNING in kvm_set_vm_id_reg
   - 发件人: Marc Zyngier <maz@kernel.org>

---

